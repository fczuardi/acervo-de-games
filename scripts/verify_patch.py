#!/usr/bin/env python3
"""Fingerprint an assembled PlayStation retail patch in one sequential read."""

import argparse
import datetime
import hashlib
import json
import os
import sys
import time
from pathlib import Path


BLOCK_SIZE = 16 * 1024 * 1024
HASH_BY_LENGTH = {40: "sha1", 64: "sha256"}


def write_atomic(path: Path, content: str) -> None:
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as stream:
        stream.write(content)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def piece_algorithm(piece: dict, index: int) -> str:
    expected = piece.get("hashValue", "")
    algorithm = HASH_BY_LENGTH.get(len(expected))
    if algorithm is None or any(
        character not in "0123456789abcdefABCDEF" for character in expected
    ):
        fail(f"piece {index} has an unsupported hashValue")
    return algorithm


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Calculate the complete PKG SHA-256 and verify every manifest byte "
            "range during the same sequential read."
        )
    )
    parser.add_argument("manifest", type=Path, help="original Sony manifest JSON")
    parser.add_argument("package", type=Path, help="assembled retail PKG")
    parser.add_argument("report", type=Path, help="destination piece-report TSV")
    parser.add_argument("summary", type=Path, help="destination verification JSON")
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    with args.manifest.open("rb") as stream:
        manifest_bytes = stream.read()
    manifest_sha256 = hashlib.sha256(manifest_bytes).hexdigest()
    manifest = json.loads(manifest_bytes)

    pieces = manifest.get("pieces", [])
    declared_piece_count = manifest.get("numberOfSplitFiles")
    if len(pieces) != declared_piece_count:
        fail(
            f"manifest contains {len(pieces)} pieces but declares "
            f"{declared_piece_count}"
        )

    expected_offset = 0
    for index, piece in enumerate(pieces):
        piece_algorithm(piece, index)
        if piece["fileOffset"] != expected_offset:
            fail(
                f"piece {index} begins at {piece['fileOffset']}; "
                f"expected {expected_offset}"
            )
        expected_offset += piece["fileSize"]

    expected_size = manifest.get("originalFileSize")
    package_size = args.package.stat().st_size
    if expected_offset != expected_size:
        fail("piece sizes do not sum to originalFileSize")
    if package_size != expected_size:
        fail(
            f"PKG size {package_size} does not match manifest size {expected_size}"
        )

    package_hash = hashlib.sha256()
    actual_piece_hashes: list[tuple[str, str]] = []
    bytes_read = 0
    started = time.monotonic()

    with args.package.open("rb", buffering=0) as package:
        for index, piece in enumerate(pieces):
            algorithm = piece_algorithm(piece, index)
            piece_hash = hashlib.new(algorithm)
            remaining = piece["fileSize"]
            while remaining:
                block = package.read(min(BLOCK_SIZE, remaining))
                if not block:
                    fail(f"unexpected end of file in piece {index}")
                package_hash.update(block)
                piece_hash.update(block)
                block_size = len(block)
                remaining -= block_size
                bytes_read += block_size

            actual_piece_hashes.append((algorithm, piece_hash.hexdigest()))
            elapsed = time.monotonic() - started
            rate = bytes_read / elapsed / (1024 * 1024)
            print(
                f"piece {index + 1}/{len(pieces)}: "
                f"{bytes_read}/{package_size} bytes, {rate:.1f} MiB/s",
                file=sys.stderr,
                flush=True,
            )

        if package.read(1):
            fail("data found after expected end of PKG")

    rows = ["index\toffset\tsize\thash_algorithm\texpected_hash\tactual_hash\tstatus\n"]
    matches = 0
    for index, (piece, (algorithm, actual_hash)) in enumerate(
        zip(pieces, actual_piece_hashes, strict=True)
    ):
        expected_hash = piece["hashValue"].lower()
        status = "ok" if actual_hash == expected_hash else "mismatch"
        matches += status == "ok"
        rows.append(
            f"{index}\t{piece['fileOffset']}\t{piece['fileSize']}\t"
            f"{algorithm}\t{expected_hash}\t{actual_hash}\t{status}\n"
        )

    if matches != len(pieces):
        fail(f"only {matches}/{len(pieces)} piece hashes matched; no files written")

    elapsed = time.monotonic() - started
    report_content = "".join(rows)
    report_sha256 = hashlib.sha256(report_content.encode("utf-8")).hexdigest()
    verified_at = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    summary = {
        "recordVersion": 1,
        "verifiedAt": verified_at,
        "manifest": {
            "filename": args.manifest.name,
            "size": len(manifest_bytes),
            "sha256": manifest_sha256,
        },
        "assembledRetailPackage": {
            "filename": args.package.name,
            "size": package_size,
            "sha256": package_hash.hexdigest(),
        },
        "distributionManifest": {
            "originalFileSize": expected_size,
            "numberOfSplitFiles": declared_piece_count,
            "packageDigest": manifest.get("packageDigest"),
            "playgoChunkCrcHashValue": manifest.get("playgoChunkCrcHashValue"),
        },
        "layoutValidation": {
            "pieceCountMatchesManifest": True,
            "pieceSizesSumToOriginalFileSize": True,
            "offsetsContiguous": True,
            "gaps": 0,
            "overlaps": 0,
        },
        "pieceVerification": {
            "reportFilename": args.report.name,
            "reportSha256": report_sha256,
            "hashAlgorithms": sorted(
                {algorithm for algorithm, _actual in actual_piece_hashes}
            ),
            "piecesVerified": len(pieces),
            "matches": matches,
            "mismatches": 0,
        },
        "performance": {
            "elapsedSeconds": round(elapsed, 3),
            "averageMiBPerSecond": round(package_size / elapsed / (1024 * 1024), 3),
        },
    }

    write_atomic(args.report, report_content)
    write_atomic(
        args.summary,
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
