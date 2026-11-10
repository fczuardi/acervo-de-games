# PatchDL issue #26

URL: https://github.com/knutwurst/ps5-patchdl/issues/26

State when recorded: open

Created: 2026-11-10T17:42:29Z

Title: Feature request: import and verify an existing official retail PKG

The body below matches the published issue.

## Use case

I keep a jailbroken PS5 on firmware 13.60 intentionally isolated from the
internet. For preservation, I already have an original Sony retail update PKG
and its original Sony JSON manifest stored locally. The complete PKG SHA-256
and every manifest piece have been verified outside the console.

PatchDL 0.3.12 correctly finds the compatible update for my physical disc, but
the supported workflow requires downloading the same 53 GB package again from
the Sony CDN before PatchDL can install or replace the application.

Downloading directly is useful as the default, but an offline import would
help users who already retain the official package and want to minimize network
exposure and dependence on continued CDN availability.

## Requested behavior

Could PatchDL support adopting an existing official retail PKG from local,
external or USB storage?

A possible flow:

1. Select a PKG and its original Sony manifest.
2. Validate the expected Title ID and Content ID from the package metadata.
3. Validate package size, piece count, contiguous offsets and every piece hash
   from the Sony manifest.
4. Obtain or accept the corresponding PlayGo CRC file when required.
5. Generate PatchDL's own `state.json`, local manifest and other sidecars only
   after verification succeeds.
6. Expose the same Install/Replace action as a download completed and verified
   by PatchDL.

This should not bypass PatchDL's source policy or add support for modified,
unsigned or fake packages. An imported package could use a distinct source
state such as `imported_official` and remain subject to the existing title,
content and package checks.

## Why this would help

- avoids downloading a large artifact that has already been preserved;
- lets deliberately isolated consoles stay offline;
- supports reinstalls if the CDN or third-party version index disappears;
- lets users compare the imported package with an independently recorded hash;
- keeps state and sidecar generation inside PatchDL instead of encouraging
  unsupported manual manipulation of `/data/patchdl`.

The current code already appears to contain most of the relevant primitives for
manifest parsing, per-piece verification, package metadata inspection, local
manifest generation and installation. I did not manually seed PatchDL's state
because I wanted to keep the existing workflow unmodified.

Would this fit the project's scope? Is there already a supported way to adopt a
previously downloaded retail PKG that I missed?
