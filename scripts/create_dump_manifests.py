#!/usr/bin/env python3
"""Create matching SHA-256 and apparent-size manifests for an extracted dump."""

import argparse
import fcntl
import hashlib
import os
import re
import stat
import sys
import time
from pathlib import Path


BLOCK_SIZE = 16 * 1024 * 1024


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb", buffering=0) as stream:
        while block := stream.read(BLOCK_SIZE):
            digest.update(block)
    return digest.hexdigest()


def sha256sum_path(path: str) -> tuple[str, str]:
    if "\n" in path:
        fail(f"newline cannot be represented in the size TSV: {path!r}")
    if "\t" in path:
        fail(f"tab cannot be represented in the size TSV: {path!r}")
    if "\\" in path:
        return "\\", path.replace("\\", "\\\\")
    return "", path


def write_manifest_hash(path: Path) -> str:
    return sha256_file(path)


SHA_LINE = re.compile(r"^([0-9a-f]{64})  (.*)$")


def unescape_sha256sum_path(value: str) -> str:
    output: list[str] = []
    index = 0
    while index < len(value):
        if value[index] != "\\":
            output.append(value[index])
            index += 1
            continue
        if index + 1 == len(value) or value[index + 1] not in ("\\", "n"):
            fail("invalid sha256sum filename escape")
        output.append("\n" if value[index + 1] == "n" else "\\")
        index += 2
    return "".join(output)


def read_sha_prefix(path: Path, files: list[tuple[bytes, Path, str, int]]) -> int:
    if not path.exists():
        return 0
    lines = path.read_text(encoding="utf-8").splitlines()
    parsed: list[tuple[str, str]] = []
    invalid_lines: list[int] = []
    for index, line in enumerate(lines):
        escaped = line.startswith("\\")
        if escaped:
            line = line[1:]
        match = SHA_LINE.fullmatch(line)
        if not match:
            invalid_lines.append(index + 1)
            continue
        encoded_path = match.group(2)
        decoded_path = unescape_sha256sum_path(encoded_path) if escaped else encoded_path
        parsed.append((decoded_path, match.group(1)))

    if not invalid_lines and len(parsed) <= len(files) and all(
        item[0] == files[index][2] for index, item in enumerate(parsed)
    ):
        return len(parsed)

    expected_paths = {relative for _key, _path, relative, _size in files}
    recovered: dict[str, str] = {}
    for relative, digest in parsed:
        if relative not in expected_paths:
            fail(f"unexpected path in temporary SHA-256 manifest: {relative!r}")
        previous = recovered.setdefault(relative, digest)
        if previous != digest:
            fail(f"conflicting hashes for duplicated path: {relative!r}")
    if set(recovered) != expected_paths:
        fail(
            "temporary SHA-256 manifest is neither an ordered prefix nor a "
            "complete recoverable path set"
        )

    recovered_path = path.with_name(path.name + ".recovered")
    with recovered_path.open("w", encoding="utf-8", newline="") as stream:
        for _key, _file_path, relative, _size in files:
            marker, encoded_path = sha256sum_path(relative)
            stream.write(f"{marker}{recovered[relative]}  {encoded_path}\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(recovered_path, path)
    print(
        f"recovered canonical SHA-256 manifest from {len(parsed)} lines "
        f"covering {len(files)} unique paths; ignored malformed lines: "
        f"{len(invalid_lines)}",
        flush=True,
    )
    return len(files)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("game_dir", type=Path, help="root of the extracted game")
    parser.add_argument("output_dir", type=Path, help="directory beside the game tree")
    parser.add_argument("stem", help="output filename stem")
    parser.add_argument(
        "--replace",
        action="store_true",
        help="replace manifests from an explicitly repeated run",
    )
    args = parser.parse_args()

    game_dir = args.game_dir.resolve()
    output_dir = args.output_dir.resolve()
    if not game_dir.is_dir():
        fail(f"game directory does not exist: {game_dir}")
    if game_dir == output_dir or game_dir in output_dir.parents:
        fail("output directory must be outside the extracted game tree")
    output_dir.mkdir(parents=True, exist_ok=True)

    sha_output = output_dir / f"{args.stem}.sha256"
    size_output = output_dir / f"{args.stem}.sizes.tsv"
    sha_temporary = sha_output.with_name(sha_output.name + ".tmp")
    size_temporary = size_output.with_name(size_output.name + ".tmp")
    lock_path = output_dir / f".{args.stem}.manifests.lock"
    lock_stream = lock_path.open("w")
    try:
        fcntl.flock(lock_stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except BlockingIOError:
        fail(f"another manifest process holds the lock: {lock_path}")
    if not args.replace:
        for path in (sha_output, size_output):
            if path.exists():
                fail(f"refusing to overwrite existing manifest: {path}")

    files: list[tuple[bytes, Path, str, int]] = []
    tabs = 0
    newlines = 0
    for root, directories, filenames in os.walk(game_dir):
        root_path = Path(root)
        if root_path == game_dir:
            directories[:] = [name for name in directories if name != "sce_sys"]
        for filename in filenames:
            path = root_path / filename
            file_stat = path.stat(follow_symlinks=False)
            if not stat.S_ISREG(file_stat.st_mode):
                continue
            relative = "./" + path.relative_to(game_dir).as_posix()
            tabs += "\t" in relative
            newlines += "\n" in relative
            files.append((os.fsencode(relative), path, relative, file_stat.st_size))

    files.sort(key=lambda item: item[0])
    print(f"files={len(files)} tabs={tabs} newlines={newlines}", flush=True)
    if tabs or newlines:
        fail("TSV is unsafe for these filenames; no manifests written")

    resume_index = read_sha_prefix(sha_temporary, files)
    if resume_index:
        print(f"resuming after {resume_index} validated SHA-256 entries", flush=True)

    started = time.monotonic()
    apparent_bytes = sum(size for _key, _path, _relative, size in files)
    try:
        with (
            sha_temporary.open("a", encoding="utf-8", newline="") as sha_stream,
            size_temporary.open("w", encoding="utf-8", newline="") as size_stream,
        ):
            for index, (_sort_key, path, relative, size) in enumerate(files, start=1):
                size_stream.write(f"{size}\t{relative}\n")
                if index <= resume_index:
                    continue
                digest = sha256_file(path)
                marker, encoded_path = sha256sum_path(relative)
                sha_stream.write(f"{marker}{digest}  {encoded_path}\n")
                if index % 10_000 == 0 or index == len(files):
                    sha_stream.flush()
                    elapsed = time.monotonic() - started
                    print(
                        f"files {index}/{len(files)}; "
                        f"apparent bytes {apparent_bytes}; elapsed {elapsed:.1f}s",
                        flush=True,
                    )
            sha_stream.flush()
            size_stream.flush()
            os.fsync(sha_stream.fileno())
            os.fsync(size_stream.fileno())

        sha_lines = sum(1 for _line in sha_temporary.open("rb"))
        size_lines = sum(1 for _line in size_temporary.open("rb"))
        if sha_lines != len(files) or size_lines != len(files):
            fail("manifest entry count differs from the source path set")

        os.replace(sha_temporary, sha_output)
        os.replace(size_temporary, size_output)
    except BaseException:
        print("incomplete manifests retain the .tmp suffix", file=sys.stderr)
        raise

    print(f"hashedFiles={len(files)}")
    print(f"apparentBytes={apparent_bytes}")
    print(f"sha256Manifest={write_manifest_hash(sha_output)}")
    print(f"sizeManifestSha256={write_manifest_hash(size_output)}")
    print(f"sha256Path={sha_output}")
    print(f"sizePath={size_output}")
    lock_stream.close()
    lock_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
