# Tombstone — Ratchet & Clank: Rift Apart 01.005.003

Registro do dump atualizado descriptografado de *Ratchet & Clank: Rift Apart*
para PS5, removido depois da preservação do retail PKG, dos fingerprints e de
uma working copy FFPKG funcional.

## Identificação

- Title ID: `PPSA01473`
- Content ID: `UP9000-PPSA01473_00-RATCHETCLANKRIFT`
- Versão: `01.005.003`
- Master Version: `01.00`
- Firmware mínimo codificado: `0x1020000000000000`
- Extração antiga: sem `dump-info.json` e sem log específico preservado

## Evidência preservada

Os manifestos excluem `sce_sys/`, conforme o protocolo da coleção, e registram
171 arquivos regulares e 73.045.535.492 bytes aparentes:

- `PPSA01473-01.005.003.sha256`: SHA-256
  `98ef1d0498933acd27e8b4867511830dcc5b62f35dcfb74d73544b621bd48495`
- `PPSA01473-01.005.003.sizes.tsv`: SHA-256
  `1db5f3a2ac16517f5031e8c732dc29d549d3b6f5fbc9a42cfb6c25f2d26aa746`
- `param.json`: 5.127 bytes; SHA-256
  `8612e99503645267e46115fa1b42d84d1a775e02a40a85fc79791cb7a5257f0a`

A working copy FFPKG de 37.576.966.144 bytes foi executada com sucesso no
console. Seu SHA-256 é
`4cb15dd0f68c2302646eaef9856ef865cdd06a9e2a135d9dadf9b0eff81b2473`.

## Motivo e disposição

A coleção mantém o dump-base `01.000.000`, o retail PKG oficial
`01.005.003`, os fingerprints dos dois dumps e a working copy validada. O
payload atualizado pode ser reproduzido a partir desses materiais e foi
removido para recuperar espaço.

- Decisão e remoção do payload: 21 de novembro de 2026
- Payload removido: árvore `PPSA01473-app0_Ratchet_&_Clank_Rift_Apart`
- Dados mantidos: este tombstone, `param.json` e os dois manifestos completos
