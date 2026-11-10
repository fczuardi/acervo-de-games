#!/usr/bin/env python3
"""Create the aggregate checksum manifest without rereading the retail PKG."""

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def write_atomic(path: Path, content: str) -> None:
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as stream:
        stream.write(content)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def write_json_atomic(path: Path, value: object) -> None:
    write_atomic(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("patch_dir", type=Path)
    parser.add_argument("stem")
    args = parser.parse_args()
    directory = args.patch_dir.resolve()
    stem = args.stem

    verification_path = directory / f"{stem}.verification.json"
    with verification_path.open(encoding="utf-8") as stream:
        verification = json.load(stream)
    package = directory / f"{stem}.pkg"
    package_record = verification["assembledRetailPackage"]
    if package.name != package_record["filename"]:
        fail("verification record names a different package")
    if package.stat().st_size != package_record["size"]:
        fail("package size differs from the verification record")

    acquisition_path = directory / f"{stem}.acquisition.json"
    with acquisition_path.open(encoding="utf-8") as stream:
        acquisition = json.load(stream)
    acquisition_package = acquisition["assembledRetailPackage"]
    existing_hash = acquisition_package.get("sha256")
    if existing_hash not in (None, package_record["sha256"]):
        fail("package SHA-256 differs between acquisition and verification records")
    acquisition_package["sha256"] = package_record["sha256"]
    acquisition_package["hashSource"] = (
        f"{verification_path.name}; calculated during package verification"
    )
    acquisition_package.pop("note", None)
    write_json_atomic(acquisition_path, acquisition)

    names = [
        acquisition_path.name,
        f"{stem}.json",
        f"{stem}.manifest.sha256",
        f"{stem}.pieces.sha256.tsv",
        f"{stem}.verification.json",
    ]
    rows = []
    for name in names:
        path = directory / name
        if not path.is_file():
            fail(f"required artifact is missing: {name}")
        rows.append((name, sha256_file(path)))
    rows.append((package.name, package_record["sha256"]))
    rows.sort(key=lambda item: item[0].encode("utf-8"))

    output = directory / f"{stem}.artifacts.sha256"
    write_atomic(output, "".join(f"{digest}  {name}\n" for name, digest in rows))
    print(f"completed: {output}")
    print("The PKG was checked by size; its recorded SHA-256 was reused.")


if __name__ == "__main__":
    main()
