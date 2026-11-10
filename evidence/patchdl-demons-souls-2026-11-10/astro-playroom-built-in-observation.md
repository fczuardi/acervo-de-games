# ASTRO's PLAYROOM as a built-in PS5 replacement case

Observed in PatchDL v0.3.12 while Demon's Souls was downloading:

- Title ID: `PPSA01325`
- Installed version: none
- Offered version: `01.905.000`
- UI action: Install

This is an explicit special case in `src/patchdl_websrv.c:5162-5191`.
`add_builtin_titles()` adds ASTRO's PLAYROOM when it is absent because it ships
with every PS5 and can otherwise be unavailable to an offline console after a
restore. The entry is marked `PATCHDL_SOURCE_OFFICIAL` and `builtin = 1`.

Immediately below it, the source describes completed PS5 downloads whose game
is absent as installable because a PS5 update is treated as the whole game
(`src/patchdl_websrv.c:5201-5203`).

This corroborates the technical model behind the Demon's Souls replacement:
PatchDL expects a PS5 retail update package to be installable after the prior
application is removed. It does not establish universal licensing behavior.
ASTRO's PLAYROOM is bundled with the console, while Demon's Souls is expected
to continue using the physical disc as its license.

The observation was made in the web UI. A simultaneous diagnostic API request
returned an empty response while PatchDL was busy downloading; no state-changing
request was made.
