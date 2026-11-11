#!/usr/bin/env python3
"""Download a split Sony retail patch with per-piece verification and resume."""

import argparse
import datetime
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlsplit


BLOCK_SIZE = 16 * 1024 * 1024
HASH_BY_LENGTH = {40: "sha1", 64: "sha256"}
SONY_PRIVATE_CA_HOSTS = {"sgst.prod.dl.playstation.net"}
SONY_PRIVATE_CA = Path(__file__).resolve().parent / "certs" / "scei-dnas-root-05.pem"


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def write_atomic(path: Path, content: str) -> None:
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as stream:
        stream.write(content)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def hash_file(path: Path, algorithm: str, limit: int | None = None) -> str:
    digest = hashlib.new(algorithm)
    remaining = limit
    with path.open("rb") as stream:
        while remaining is None or remaining:
            size = BLOCK_SIZE if remaining is None else min(BLOCK_SIZE, remaining)
            block = stream.read(size)
            if not block:
                break
            digest.update(block)
            if remaining is not None:
                remaining -= len(block)
    if remaining not in (None, 0):
        fail(f"unexpected end of file while hashing {path}")
    return digest.hexdigest()


def hash_range(stream, size: int, algorithm: str) -> str:
    digest = hashlib.new(algorithm)
    remaining = size
    while remaining:
        block = stream.read(min(BLOCK_SIZE, remaining))
        if not block:
            fail("unexpected end of assembled partial while checking a piece")
        digest.update(block)
        remaining -= len(block)
    return digest.hexdigest()


def piece_algorithm(piece: dict, index: int) -> str:
    expected = piece.get("hashValue", "")
    algorithm = HASH_BY_LENGTH.get(len(expected))
    if algorithm is None or any(char not in "0123456789abcdefABCDEF" for char in expected):
        fail(f"piece {index} has an unsupported hashValue")
    return algorithm


def curl_version() -> str | None:
    result = subprocess.run(
        ["curl", "--version"], check=False, capture_output=True, text=True
    )
    return result.stdout.splitlines()[0] if result.returncode == 0 else None


def download_piece(url: str, destination: Path) -> None:
    command = [
        "curl",
        "--fail",
        "--location",
        "--retry",
        "10",
        "--retry-all-errors",
        "--continue-at",
        "-",
        "--output",
        str(destination),
    ]
    if urlsplit(url).hostname in SONY_PRIVATE_CA_HOSTS:
        if not SONY_PRIVATE_CA.is_file():
            fail(f"Sony private CA certificate is missing: {SONY_PRIVATE_CA}")
        command.extend(
            [
                "--cacert",
                str(SONY_PRIVATE_CA),
                "--tls-max",
                "1.2",
                "--ciphers",
                "DEFAULT:@SECLEVEL=0",
            ]
        )
    command.append(url)
    result = subprocess.run(command, check=False)
    if result.returncode:
        fail(
            f"curl exited with status {result.returncode}; resumable piece retained at "
            f"{destination}"
        )


def append_piece(piece_path: Path, partial: Path) -> None:
    with partial.open("ab", buffering=0) as output, piece_path.open("rb") as source:
        shutil.copyfileobj(source, output, BLOCK_SIZE)
        output.flush()
        os.fsync(output.fileno())


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Download and assemble manifest pieces with retries, resume and "
            "SHA-1/SHA-256 piece verification."
        )
    )
    parser.add_argument("manifest", type=Path, help="retained Sony manifest JSON")
    parser.add_argument("output", type=Path, help="final assembled PKG path")
    parser.add_argument(
        "--discard-incomplete-tail",
        action="store_true",
        help=(
            "after verifying every complete leading piece, truncate an existing "
            "assembled .part file back to the last piece boundary"
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    manifest_path = args.manifest.resolve()
    output = args.output.resolve()
    partial = output.with_name(output.name + ".part")
    acquisition = output.with_suffix(".acquisition.json")

    if output.exists():
        fail(f"refusing to overwrite completed output: {output}")
    if acquisition.exists():
        fail(f"refusing to overwrite acquisition record: {acquisition}")
    if not manifest_path.is_file():
        fail(f"manifest does not exist: {manifest_path}")

    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    pieces = manifest.get("pieces")
    declared_count = manifest.get("numberOfSplitFiles")
    expected_size = manifest.get("originalFileSize")
    if not isinstance(pieces, list) or not pieces:
        fail("manifest has no pieces")
    if declared_count != len(pieces):
        fail(f"manifest declares {declared_count} pieces but contains {len(pieces)}")
    if not isinstance(expected_size, int) or expected_size < 1:
        fail("manifest has no valid originalFileSize")

    boundary = 0
    for index, piece in enumerate(pieces):
        if piece.get("fileOffset") != boundary:
            fail(f"piece {index} is not contiguous at offset {boundary}")
        size = piece.get("fileSize")
        if not isinstance(size, int) or size < 1:
            fail(f"piece {index} has no valid fileSize")
        if not isinstance(piece.get("url"), str) or not piece["url"]:
            fail(f"piece {index} has no URL")
        piece_algorithm(piece, index)
        boundary += size
    if boundary != expected_size:
        fail("piece sizes do not sum to originalFileSize")

    output.parent.mkdir(parents=True, exist_ok=True)
    manifest_digest = hashlib.sha256(manifest_bytes).hexdigest()
    manifest_checksum = manifest_path.with_suffix(".manifest.sha256")
    checksum_content = f"{manifest_digest}  {manifest_path.name}\n"
    if manifest_checksum.exists():
        if manifest_checksum.read_text(encoding="utf-8") != checksum_content:
            fail(f"retained manifest checksum differs: {manifest_checksum}")
    else:
        write_atomic(manifest_checksum, checksum_content)

    partial_size = partial.stat().st_size if partial.exists() else 0
    if partial_size > expected_size:
        fail(f"assembled partial is larger than the manifest: {partial_size}")

    complete_count = 0
    complete_boundary = 0
    for piece in pieces:
        end = piece["fileOffset"] + piece["fileSize"]
        if end > partial_size:
            break
        complete_count += 1
        complete_boundary = end

    if complete_count:
        print(f"checking {complete_count} complete piece(s) already assembled")
        with partial.open("rb") as stream:
            for index in range(complete_count):
                piece = pieces[index]
                actual = hash_range(
                    stream, piece["fileSize"], piece_algorithm(piece, index)
                )
                expected = piece["hashValue"].lower()
                if actual != expected:
                    fail(
                        f"existing assembled piece {index} mismatches: "
                        f"actual {actual}, expected {expected}"
                    )
                print(f"existing piece {index + 1}/{len(pieces)}: OK")

    if partial_size != complete_boundary:
        tail_size = partial_size - complete_boundary
        if not args.discard_incomplete_tail:
            fail(
                f"assembled partial has an incomplete tail of {tail_size} bytes; "
                "rerun with --discard-incomplete-tail after reviewing this message"
            )
        print(
            f"discarding incomplete tail: {tail_size} bytes; "
            f"keeping {complete_boundary} verified bytes"
        )
        with partial.open("r+b") as stream:
            stream.truncate(complete_boundary)
            stream.flush()
            os.fsync(stream.fileno())

    started = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    resumed_bytes = complete_boundary
    for index in range(complete_count, len(pieces)):
        piece = pieces[index]
        piece_partial = output.with_name(output.name + f".piece-{index:02d}.part")
        if piece_partial.exists() and piece_partial.stat().st_size > piece["fileSize"]:
            fail(f"piece partial is larger than expected: {piece_partial}")
        print(
            f"downloading piece {index + 1}/{len(pieces)} "
            f"({piece['fileSize']} bytes)"
        )
        download_piece(piece["url"], piece_partial)
        actual_size = piece_partial.stat().st_size
        if actual_size != piece["fileSize"]:
            fail(
                f"piece {index} size is {actual_size}; expected {piece['fileSize']}; "
                f"partial retained at {piece_partial}"
            )
        algorithm = piece_algorithm(piece, index)
        actual_hash = hash_file(piece_partial, algorithm)
        expected_hash = piece["hashValue"].lower()
        if actual_hash != expected_hash:
            fail(
                f"piece {index} {algorithm} mismatch: actual {actual_hash}, "
                f"expected {expected_hash}; file retained at {piece_partial}"
            )
        append_piece(piece_partial, partial)
        piece_partial.unlink()
        assembled_size = partial.stat().st_size
        expected_boundary = piece["fileOffset"] + piece["fileSize"]
        if assembled_size != expected_boundary:
            fail(
                f"assembled size is {assembled_size}; expected {expected_boundary}"
            )
        print(f"piece {index + 1}/{len(pieces)}: verified and assembled")

    if partial.stat().st_size != expected_size:
        fail("assembled package did not reach originalFileSize")

    finished = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    url_set = "\n".join(piece["url"] for piece in pieces).encode("utf-8")
    algorithms = sorted({piece_algorithm(piece, i) for i, piece in enumerate(pieces)})
    record = {
        "recordVersion": 1,
        "started": started,
        "finished": finished,
        "resumedFromBytes": resumed_bytes,
        "manifest": {
            "filename": manifest_path.name,
            "size": len(manifest_bytes),
            "sha256": manifest_digest,
            "originalFileSize": expected_size,
            "numberOfSplitFiles": declared_count,
        },
        "assembledRetailPackage": {
            "filename": output.name,
            "size": expected_size,
            "sha256": None,
            "note": "SHA-256 is calculated later by the single-pass verifier.",
        },
        "source": {
            "pieceUrlSetSha256": hashlib.sha256(url_set).hexdigest(),
            "urlCount": len(pieces),
            "urlsRetained": False,
        },
        "acquisitionTool": {
            "name": "download_patch_resumable.py + curl",
            "scriptFilename": Path(__file__).name,
            "scriptSha256": hash_file(Path(__file__).resolve(), "sha256"),
            "curlVersion": curl_version(),
            "pieceHashAlgorithms": algorithms,
            "retryCountPerInvocation": 10,
            "retryDelayPolicy": "curl default exponential backoff",
            "sonyPrivateCaFilename": SONY_PRIVATE_CA.name,
            "sonyLegacyTlsPolicy": "TLS <=1.2; OpenSSL SECLEVEL=0; peer and hostname verification enabled",
        },
    }

    os.replace(partial, output)
    write_atomic(acquisition, json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    print(f"completed: {output}")
    print(f"acquisition record: {acquisition}")


if __name__ == "__main__":
    main()
