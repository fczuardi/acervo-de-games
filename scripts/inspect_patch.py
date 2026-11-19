#!/usr/bin/env python3
"""Fetch and inspect a Sony PS5 split-package manifest without downloading its PKG."""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


TITLE_ID = re.compile(r"PPSA\d{5}")


def fail(message: str) -> None:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


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
            fail("URL must end in _sc.pkg, -DP.pkg, _0.pkg, or .json")
    return urlunsplit((parts.scheme, parts.netloc, path, parts.query, parts.fragment))


def write_atomic(path: Path, data: bytes) -> None:
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temporary, path)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Retain and inspect only the Sony JSON manifest for a PS5 patch."
    )
    parser.add_argument("url", help="Sony _sc.pkg, -DP.pkg, _0.pkg, or manifest URL")
    parser.add_argument("output", type=Path, help="destination .json manifest")
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    output = args.output.resolve()
    checksum = output.with_name(output.stem + ".manifest.sha256")
    url = manifest_url(args.url)

    ca_file = Path(__file__).with_name("certs") / "scei-dnas-root-05.pem"
    result = subprocess.run(
        [
            "curl", "--fail", "--location", "--silent", "--show-error",
            "--retry", "3", "--retry-all-errors", "--retry-delay", "2",
            "--user-agent", "Mozilla/5.0", "--cacert", str(ca_file),
            "--tls-max", "1.2", "--ciphers", "DEFAULT:@SECLEVEL=0", url,
        ],
        check=False,
        capture_output=True,
    )
    if result.returncode:
        fail(
            "could not fetch Sony manifest: "
            + result.stderr.decode("utf-8", errors="replace").strip()
        )
    data = result.stdout

    try:
        manifest = json.loads(data)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        fail(f"response is not valid JSON: {error}")

    size = manifest.get("originalFileSize")
    count = manifest.get("numberOfSplitFiles")
    pieces = manifest.get("pieces")
    if not isinstance(size, int) or size <= 0:
        fail("manifest has no valid originalFileSize")
    if not isinstance(count, int) or not isinstance(pieces, list) or count != len(pieces):
        fail("manifest piece count is invalid")

    expected_offset = 0
    piece_ids: set[str] = set()
    for number, piece in enumerate(pieces, 1):
        if not isinstance(piece, dict):
            fail(f"piece {number} is not an object")
        offset = piece.get("fileOffset")
        piece_size = piece.get("fileSize")
        piece_url = piece.get("url")
        digest = piece.get("hashValue")
        if offset != expected_offset or not isinstance(piece_size, int) or piece_size <= 0:
            fail(f"piece {number} has invalid or non-contiguous layout")
        if not isinstance(piece_url, str) or not isinstance(digest, str):
            fail(f"piece {number} has invalid URL or hash")
        expected_offset += piece_size
        piece_ids.update(TITLE_ID.findall(piece_url))
    if expected_offset != size:
        fail(f"piece sizes total {expected_offset}, expected {size}")

    if output.exists() and output.read_bytes() != data:
        fail(f"refusing to overwrite different manifest: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    write_atomic(output, data)
    digest = hashlib.sha256(data).hexdigest()
    checksum_line = f"{digest}  {output.name}\n".encode()
    if checksum.exists() and checksum.read_bytes() != checksum_line:
        fail(f"refusing to overwrite different checksum: {checksum}")
    write_atomic(checksum, checksum_line)

    source_ids = set(TITLE_ID.findall(args.url))
    print(f"manifest: {output}")
    print(f"manifest SHA-256: {digest}")
    print(f"package size: {size} bytes ({size / 1_000_000_000:.3f} GB; {size / 2**30:.3f} GiB)")
    print(f"pieces: {count}; contiguous: yes; total matches: yes")
    print(f"source Title ID(s): {', '.join(sorted(source_ids)) or 'none'}")
    print(f"piece Title ID(s): {', '.join(sorted(piece_ids)) or 'none'}")
    if piece_ids - source_ids:
        print("warning: one or more piece Title IDs differ from the source URL")


if __name__ == "__main__":
    main()
