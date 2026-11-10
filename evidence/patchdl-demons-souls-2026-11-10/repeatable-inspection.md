# Repeatable filesystem inspection

Use this inspection immediately before the controlled replacement and again
after the replacement has finished. It is read-only and requires no new PS5
homebrew beyond the existing FTP server.

For `PPSA01342`, record:

1. Existence and directory metadata for:
   - `/user/app/PPSA01342/`
   - `/user/patch/PPSA01342/`
   - `/user/appmeta/PPSA01342/`
   - the same relative paths below any applicable `/mnt/ext*` and `/mnt/usb*`
     volumes.
2. A non-recursive listing of each directory that exists.
3. A non-recursive listing of `/user/app/PPSA01342/sce_sys/` when present.
4. The contents of `mount.lnk` and `mount_img.lnk` when present, sanitizing any
   transient shadow-mount identifier before retention.
5. Only these fields from appmeta `param.json`: `titleId`, `contentId`,
   `contentVersion`, `masterVersion`, and `applicationCategoryType`.

Do not recursively enumerate game data, calculate directory hashes, retrieve
images, licenses, account data, saves, or game executables.

The same path list and field selection must be used for the post-operation
snapshot. Differences can establish whether the registered application,
appmeta, separate patch directory, mount links, version and storage target
changed. They cannot by themselves observe a short interval between PatchDL's
uninstall and install; PatchDL's own log supplies that ordering, while optional
one-second existence polling during a later run could document the transient
absence without reading game content.

## Required baseline

Before running the actual experiment, remove the ShadowMount registration by
its normal UI workflow and establish the intended official disc installation.
Then repeat this inspection. Do not treat the snapshot already collected as an
official disc-install baseline.
