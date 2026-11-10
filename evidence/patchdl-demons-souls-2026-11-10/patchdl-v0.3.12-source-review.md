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

## Distinction from the executed experiment

The automatic replacement path described above was not invoked in the
subsequent Demon's Souls experiment. After the package download, the UI offered
only **Install**. The inspected package metadata reported the installed base
and expected package base as `01.000.000`, with `base_fits` true, so that action
would perform the normal update install over a compatible base rather than
enter `do_replace_install()`.

To establish an unambiguous patch-only starting condition, the base application
was therefore deleted through the native PS5 UI. Its absence was confirmed by
read-only FTP inspection before PatchDL was restarted and offered **Install
01.007.000** for the now-uninstalled title. The experiment demonstrates the
result of installing that orphaned update package; it does not demonstrate the
automatic replacement routine end to end.
