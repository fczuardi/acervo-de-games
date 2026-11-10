# Failed standalone installation without the disc

PatchDL v0.3.12 recognized the completed orphan download of Demon's Souls
`01.007.000` and offered **Install** while no base application was present.
The physical disc was ejected.

After **Install** was pressed, the native PS5 notification reported
`Can't install`, error `NW-102261-2`, followed by: `Can't connect to the
server. There might have been a problem connecting to the network or to our
online services.` The available actions were More Info, Suggested Actions and
Try Again.

Read-only observations after the failure:

- `/user/app/PPSA01342/`: absent;
- `/user/patch/PPSA01342/`: absent;
- `/user/appmeta/PPSA01342/`: created;
- retained appmeta `param.json` reports version `01.007.000`;
- the complete PKG, local manifest, CRC and `state.json` remained in
  `/data/patchdl/PPSA01342/`;
- PatchDL's HTTP server on port 12880 was no longer reachable immediately
  after the failure.

The path monitor observed appmeta transition from absent to present at
`2026-11-10T15:05:03.329-03:00`, while app and patch remained absent.

The PatchDL-generated local manifest points every package range and the PlayGo
CRC at `http://127.0.0.1:12880/api/pkg/...`. The native error and the observed
loss of that listener therefore point to interruption of PatchDL's local HTTP
server, not to a demonstrated disc-license failure.

This establishes that package metadata was materialized before the local
delivery path failed. It does not establish whether the physical disc is
required during installation.
