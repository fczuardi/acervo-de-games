# PatchDL v0.3.12 source review

Reviewed: 2026-11-10

Source: `knutwurst/ps5-patchdl`, tag `v0.3.12`

Commit: `8a281f07dc911e954e81fcf285d91e773e85a53e`

## Replacement behavior

For a PS5 replacement, `do_replace_install()` starts `replace_thread()` with
`patch_only` false. The thread calls `patchdl_install_uninstall()`, waits until
`replace_old_gone()` reports that the prior application has disappeared, and
only then calls `patchdl_install_local_pkg()`.

`patchdl_install_uninstall()` reaches `sceAppInstUtilAppUnInstall`. The distinct
`sceAppInstUtilAppUnInstallPat` path is selected only when `patch_only` is true,
which the source identifies as the PS4 downgrade case.

The source therefore establishes PatchDL's intended ordering and API choice:
full PS5 application uninstall, confirmation that the old application is gone,
then installation of the downloaded package. It does not by itself prove which
filesystem paths the proprietary system API removes on this console.

Relevant source locations in this revision:

- `src/patchdl_websrv.c:3653` — replacement thread and wait;
- `src/patchdl_websrv.c:3701` — PS5 whole-game replacement description;
- `src/patchdl_websrv.c:3780` — PS5 title held while absent;
- `src/patchdl_install.c:822` — selection of application or patch uninstall;
- `src/patchdl_install.c:861` — full application uninstall wrapper;
- `README.md:86` — documented PS5 versus PS4 replacement behavior;
- `README.md:95` — disc remains the license after PS5 replacement.

No PatchDL operation was invoked during this review.
