#!/usr/bin/env python3
"""Create or validate the retained SHA-256 checksum for a Sony manifest."""

import argparse
import hashlib
import os
import sys
from pathlib import Path


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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("patch_dir", type=Path)
    parser.add_argument("stem")
    args = parser.parse_args()

    directory = args.patch_dir.resolve()
    manifest = directory / f"{args.stem}.json"
    checksum = directory / f"{args.stem}.manifest.sha256"
    if not manifest.is_file():
        fail(f"manifest does not exist: {manifest}")

    digest = hashlib.sha256(manifest.read_bytes()).hexdigest()
    expected = f"{digest}  {manifest.name}\n"
    if checksum.exists():
        if checksum.read_text(encoding="utf-8") != expected:
            fail(f"existing manifest checksum is invalid: {checksum}")
        print(f"verified: {checksum}")
        return

    write_atomic(checksum, expected)
    print(f"created: {checksum}")


if __name__ == "__main__":
    main()
