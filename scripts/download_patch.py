#!/usr/bin/env python3
"""Safely run fetchpkg and retain a small acquisition record."""

import argparse
import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


BLOCK_SIZE = 1024 * 1024


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(BLOCK_SIZE):
            digest.update(block)
    return digest.hexdigest()


def command_output(command: list[str]) -> str | None:
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    if result.returncode:
        return None
    return result.stdout.strip()


def write_atomic(path: Path, content: str) -> None:
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as stream:
        stream.write(content)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Download a retail patch with fetchpkg through a non-resumable .part "
            "file, validate its size, and record acquisition-tool metadata."
        )
    )
    parser.add_argument("fetchpkg", type=Path, help="fetchpkg executable")
    parser.add_argument("manifest", type=Path, help="retained Sony manifest JSON")
    parser.add_argument("output", type=Path, help="final assembled PKG path")
    parser.add_argument("url", help="Sony supplemental PKG or manifest URL")
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    fetchpkg = args.fetchpkg.resolve()
    manifest_path = args.manifest.resolve()
    output = args.output.resolve()
    partial = output.with_name(output.name + ".part")
    acquisition = output.with_suffix(".acquisition.json")

    if not fetchpkg.is_file() or not os.access(fetchpkg, os.X_OK):
        fail(f"fetchpkg is not an executable file: {fetchpkg}")
    if output.exists():
        fail(f"refusing to overwrite completed output: {output}")
    if partial.exists():
        fail(
            f"partial output already exists: {partial}; fetchpkg cannot resume, "
            "so inspect or remove it explicitly before retrying"
        )
    if acquisition.exists():
        fail(f"refusing to overwrite acquisition record: {acquisition}")

    with manifest_path.open("rb") as stream:
        manifest_bytes = stream.read()
    manifest = json.loads(manifest_bytes)
    expected_size = manifest.get("originalFileSize")
    if not isinstance(expected_size, int) or expected_size < 1:
        fail("manifest has no valid originalFileSize")

    output.parent.mkdir(parents=True, exist_ok=True)
    started = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    result = subprocess.run(
        [str(fetchpkg), "-o", str(partial), args.url],
        check=False,
    )
    finished = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    if result.returncode:
        fail(
            f"fetchpkg exited with status {result.returncode}; partial file retained "
            f"at {partial}"
        )
    if not partial.is_file():
        fail("fetchpkg reported success but did not create the partial output")

    actual_size = partial.stat().st_size
    if actual_size != expected_size:
        fail(
            f"downloaded size {actual_size} does not match manifest size "
            f"{expected_size}; partial file retained at {partial}"
        )

    fetchpkg_parent = fetchpkg.parent
    source_commit = command_output(
        ["git", "-C", str(fetchpkg_parent), "rev-parse", "HEAD"]
    )
    source_status = command_output(
        ["git", "-C", str(fetchpkg_parent), "status", "--short"]
    )
    file_identification = command_output(["file", "-b", str(fetchpkg)])
    url_path = urlparse(args.url).path

    record = {
        "recordVersion": 1,
        "started": started,
        "finished": finished,
        "manifest": {
            "filename": manifest_path.name,
            "size": len(manifest_bytes),
            "sha256": hashlib.sha256(manifest_bytes).hexdigest(),
            "originalFileSize": expected_size,
            "numberOfSplitFiles": manifest.get("numberOfSplitFiles"),
        },
        "assembledRetailPackage": {
            "filename": output.name,
            "size": actual_size,
            "sha256": None,
            "note": "SHA-256 is calculated later by the single-pass verifier.",
        },
        "source": {
            "urlSha256": hashlib.sha256(args.url.encode("utf-8")).hexdigest(),
            "urlBasename": Path(url_path).name,
            "urlRetained": False,
        },
        "acquisitionTool": {
            "name": "fetchpkg",
            "path": str(fetchpkg),
            "size": fetchpkg.stat().st_size,
            "sha256": sha256_file(fetchpkg),
            "fileIdentification": file_identification,
            "sourceCommit": source_commit,
            "sourceWorkingTreeClean": source_status == "" if source_status is not None else None,
            "sourceWorkingTreeStatus": source_status,
            "exitCode": result.returncode,
        },
    }

    os.replace(partial, output)
    write_atomic(
        acquisition,
        json.dumps(record, ensure_ascii=False, indent=2) + "\n",
    )
    print(f"completed: {output}")
    print(f"acquisition record: {acquisition}")


if __name__ == "__main__":
    main()
