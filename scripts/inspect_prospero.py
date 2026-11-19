#!/usr/bin/env python3
"""Inspect the patch list exposed by a Prospero Patches title page."""

from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path


BASE_URL = "https://prosperopatches.com"
USER_AGENT = "acervo-de-games-preservation/0.1"


def request(url: str, data: bytes | None = None) -> bytes:
    headers = {
        "Accept": "application/json" if data is not None else "text/html",
        "User-Agent": USER_AGENT,
    }
    if data is not None:
        # This is the content type used by the site's own JavaScript, despite
        # the body being JSON.
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    with urllib.request.urlopen(req, timeout=30) as response:
        return response.read()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="List versions, sizes and firmware requirements without downloading a PKG."
    )
    parser.add_argument("title_id", help="PS5 Title ID, for example PPSA01280")
    parser.add_argument("--output", type=Path, help="optionally retain the API response as JSON")
    args = parser.parse_args()

    title_id = args.title_id.upper()
    if not re.fullmatch(r"PPSA[0-9]{5}", title_id):
        parser.error("title_id must look like PPSA01280")

    page_url = f"{BASE_URL}/{title_id}"
    try:
        html = request(page_url).decode("utf-8", errors="replace")
        match = re.search(
            rf'id="dynpatch"[^>]*data-titleid="{re.escape(title_id)}"[^>]*data-key="([0-9a-f]{{64}})"',
            html,
        )
        if not match:
            raise RuntimeError("could not find the dynamic patch-list key in the title page")

        payload = json.dumps({"titleid": title_id, "key": match.group(1)}, separators=(",", ":")).encode()
        result = json.loads(request(f"{BASE_URL}/api/internal/loadpatches", payload))
    except (OSError, urllib.error.URLError, json.JSONDecodeError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if not result.get("success"):
        print(json.dumps(result, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1

    record = {
        "source": page_url,
        "titleId": title_id,
        "queriedPatchCount": result.get("count", len(result.get("patches", []))),
        "sourceLastUpdated": result.get("lastupdated"),
        "patches": result.get("patches", []),
    }

    rendered = json.dumps(record, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"saved: {args.output}")

    print(f"{title_id}: {len(record['patches'])} version(s)")
    for patch in record["patches"]:
        latest = " latest" if patch.get("is_latest") else ""
        print(
            f"{patch.get('content_ver', '?')}\t{patch.get('filesize', '?')}\t"
            f"FW {patch.get('required_firmware', '?')}{latest}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
