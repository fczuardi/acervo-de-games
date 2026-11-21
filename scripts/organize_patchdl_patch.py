#!/usr/bin/env python3
"""Move one verified retail PKG into a canonical PatchDL-ready layout."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


TITLE_ID = re.compile(r"PPSA\d{5}")
VERSION = re.compile(r"\d{2}\.\d{3}\.\d{3}")


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


def manifest_url(source: str) -> str:
    parts = urlsplit(source)
    path = parts.path
    for suffix in ("_sc.pkg", "-DP.pkg"):
        if path.endswith(suffix):
            path = path[: -len(suffix)] + ".json"
            break
    else:
        if path.endswith("_0.pkg"):
            path = path[:-6] + ".json"
        elif not path.endswith(".json"):
            fail("last manifest piece has an unsupported filename")
    return urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))


def package_name(source: str) -> str:
    name = Path(urlsplit(source).path).name
    for suffix in ("_sc.pkg", "-DP.pkg", "_0.pkg"):
        if name.endswith(suffix):
            return name[: -len(suffix)] + ".pkg"
    fail("last manifest piece has an unsupported package filename")


def completed_bits(count: int) -> str:
    if count <= 0:
        fail("manifest has no pieces")
    return ((1 << count) - 1).to_bytes((count + 7) // 8, "little").hex()


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("patch_dir", type=Path)
    parser.add_argument("stem")
    parser.add_argument("title_id")
    parser.add_argument("name")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    directory = args.patch_dir.resolve()
    title_id = args.title_id.upper()
    if not TITLE_ID.fullmatch(title_id):
        fail("title_id must look like PPSA01234")

    version_match = VERSION.search(args.stem)
    if not version_match:
        fail("could not derive a content version from the stem")
    version = version_match.group()

    manifest_path = directory / f"{args.stem}.json"
    verification_path = directory / f"{args.stem}.verification.json"
    acquisition_path = directory / f"{args.stem}.acquisition.json"
    manifest = load_json(manifest_path)
    verification = load_json(verification_path)
    acquisition = load_json(acquisition_path)
    pieces = manifest.get("pieces")
    if not isinstance(pieces, list) or not pieces:
        fail("manifest has no pieces")
    last_url = pieces[-1].get("url")
    if not isinstance(last_url, str):
        fail("last manifest piece has no URL")

    target_name = package_name(last_url)
    if title_id not in target_name:
        fail(f"official package name does not contain {title_id}: {target_name}")
    relative_target = Path(title_id) / target_name
    target = directory / relative_target

    package_record = verification.get("assembledRetailPackage", {})
    recorded = Path(package_record.get("filename", ""))
    candidates = [directory / recorded, directory / f"{args.stem}.pkg", target]
    sources = []
    for candidate in candidates:
        if candidate.is_file() and candidate not in sources:
            sources.append(candidate)
    if len(sources) != 1:
        fail(f"expected exactly one package candidate, found {len(sources)}")
    source = sources[0]
    expected_size = manifest.get("originalFileSize")
    if source.stat().st_size != expected_size or package_record.get("size") != expected_size:
        fail("package size differs from manifest or verification record")
    digest = package_record.get("sha256")
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
        fail("verification record has no valid package SHA-256")

    state = {
        "manifest_url": manifest_url(last_url),
        "version": version,
        "name": args.name,
        "total": expected_size,
        "piece_count": len(pieces),
        "done_bytes": expected_size,
        "done": completed_bits(len(pieces)),
        "have": "",
    }
    state_path = directory / title_id / "state.json"

    print(f"source={source}")
    print(f"target={target}")
    print(f"state={state_path}")
    print(f"size={expected_size}")
    print(f"sha256={digest}")
    if not args.apply:
        print("plan only; rerun with --apply")
        return

    target.parent.mkdir(parents=True, exist_ok=True)
    if source != target:
        if target.exists():
            fail(f"target already exists: {target}")
        os.replace(source, target)

    relative = relative_target.as_posix()
    package_record["filename"] = relative
    acquisition["assembledRetailPackage"]["filename"] = relative
    write_atomic(
        verification_path,
        json.dumps(verification, ensure_ascii=False, indent=2) + "\n",
    )
    write_atomic(
        acquisition_path,
        json.dumps(acquisition, ensure_ascii=False, indent=2) + "\n",
    )
    write_atomic(state_path, json.dumps(state, ensure_ascii=False, separators=(",", ":")) + "\n")

    subprocess.run(
        [sys.executable, str(Path(__file__).with_name("finalize_patch.py")), str(directory), args.stem],
        check=True,
    )
    print("PatchDL layout applied and aggregate checksums refreshed.")


if __name__ == "__main__":
    main()
