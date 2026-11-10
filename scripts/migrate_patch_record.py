#!/usr/bin/env python3
"""Migrate the former monolithic patch record to standard split records."""

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path
from urllib.parse import urlparse


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            digest.update(block)
    return digest.hexdigest()


def write_json_atomic(path: Path, value: object) -> None:
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("legacy_record", type=Path)
    parser.add_argument("--remove-legacy", action="store_true")
    args = parser.parse_args()
    legacy_path = args.legacy_record.resolve()
    suffix = ".preservation.json"
    if not legacy_path.name.endswith(suffix):
        fail(f"legacy filename must end with {suffix}")
    stem = legacy_path.name[: -len(suffix)]
    directory = legacy_path.parent
    acquisition_path = directory / f"{stem}.acquisition.json"
    verification_path = directory / f"{stem}.verification.json"
    if acquisition_path.exists() or verification_path.exists():
        fail("split record already exists; refusing to overwrite it")

    with legacy_path.open(encoding="utf-8") as stream:
        old = json.load(stream)
    legacy_hash = sha256_file(legacy_path)
    source = old["artifacts"]["sourceManifest"]
    package = old["artifacts"]["assembledRetailPackage"]
    distribution = old["distributionManifest"]
    local = old["localPieceVerification"]
    report_hash = sha256_file(directory / local["reportFilename"])
    with (directory / source["filename"]).open(encoding="utf-8") as stream:
        source_manifest = json.load(stream)
    acquisition_url = source_manifest["pieces"][-1]["url"]

    manifest_checksum = directory / f"{stem}.manifest.sha256"
    if not manifest_checksum.exists():
        manifest_checksum.write_text(
            f"{source['sha256']}  {source['filename']}\n", encoding="utf-8"
        )

    acquisition = {
        "recordVersion": 1,
        "recordType": "retrospective",
        "acquisitionTiming": {
            "started": None,
            "finished": None,
            "packageMtime": old.get("localPackageObservation", {}).get("mtime"),
            "note": "Exact acquisition timestamps were not captured; filesystem metadata is not treated as a trusted acquisition timestamp.",
        },
        "manifest": {
            "filename": source["filename"],
            "size": source["size"],
            "sha256": source["sha256"],
            "originalFileSize": distribution["originalFileSize"],
            "numberOfSplitFiles": distribution["numberOfSplitFiles"],
        },
        "assembledRetailPackage": package | {
            "hashSource": "migrated from the former preservation record"
        },
        "source": {
            "urlSha256": hashlib.sha256(acquisition_url.encode("utf-8")).hexdigest(),
            "urlBasename": Path(urlparse(acquisition_url).path).name,
            "urlRetained": False,
            "note": "The URL is not repeated in this record; it remains in the private original Sony manifest.",
        },
        "acquisitionTool": old["acquisitionTool"],
        "migration": {"sourceFilename": legacy_path.name, "sourceSha256": legacy_hash},
    }
    verification = {
        "recordVersion": 1,
        "verifiedAt": local["verifiedAt"],
        "identity": {
            key: old[key]
            for key in ("title", "platform", "titleId", "contentId", "contentVersion")
        },
        "manifest": {key: source[key] for key in ("filename", "size", "sha256")},
        "assembledRetailPackage": package,
        "distributionManifest": distribution,
        "layoutValidation": old["layoutValidation"],
        "pieceVerification": {
            "method": local["method"],
            "reportFilename": local["reportFilename"],
            "reportSha256": report_hash,
            "piecesVerified": local["piecesVerified"],
            "matches": local["matches"],
            "mismatches": local["mismatches"],
        },
        "migration": {"sourceFilename": legacy_path.name, "sourceSha256": legacy_hash},
    }
    if "elapsedSeconds" in local:
        verification["performance"] = {
            "elapsedSeconds": local["elapsedSeconds"],
            "averageMiBPerSecond": local["averageMiBPerSecond"],
        }
    for key in ("observedPackageMetadata", "notes"):
        if key in old:
            verification[key] = old[key]

    write_json_atomic(acquisition_path, acquisition)
    write_json_atomic(verification_path, verification)
    if args.remove_legacy:
        legacy_path.unlink()
    print(f"created: {acquisition_path.name}")
    print(f"created: {verification_path.name}")
    if args.remove_legacy:
        print(f"removed: {legacy_path.name}")


if __name__ == "__main__":
    main()
