# Tombstone — Elden Ring 01.018.001 patch-only

Registro do dump descriptografado de *Elden Ring* para PS5 obtido após a
instalação patch-only do retail update `01.018.001` e removido depois da
validação e do fingerprint da working copy FFPKG.

## Identificação

- Title ID: `PPSA04610`
- Content ID: `UP0700-PPSA04610_00-ELDENRING0000000`
- Versão: `01.018.001`
- Master Version: `01.00`
- Firmware mínimo codificado: `0x1360000000000000`
- Ferramenta: PS5 App Dumper v2.10
- Estado registrado pelo dumper: `done`
- Bytes reportados pelo dumper: 156.112.555.864
- Opções: descriptografia ligada; FSELF e backport desligados; `split=3`

## Evidência preservada

Os manifestos excluem `sce_sys/`, conforme o protocolo da coleção, e registram
114.735 arquivos regulares e 156.057.680.842 bytes aparentes:

- `Elden-Ring-01.018.001-patch-only.sha256`: SHA-256
  `a6ee0cb7ca0a2bad956735d176104c567a87a8e57cd71c6b7427a5016b3e46c0`
- `Elden-Ring-01.018.001-patch-only.sizes.tsv`: SHA-256
  `02c5c2e3545467bba0354bd4f6c0e9aca952abe902ac789471cf7b1e1b1f9a4d`
- `param.json`: 2.005 bytes; SHA-256
  `beb3be7836ce101e0c8f5c6bfa55a692a40e34fdefc509734a1b601253308dda`

A working copy FFPKG de 75.301.584.896 bytes foi executada com sucesso no
console. Seu SHA-256 é
`9f0d5296153750a5eded831310d6511baa00362d262874eda8d32af1702e96a7`.

## Motivo e disposição

A coleção mantém o dump-base `01.000.000`, o retail PKG oficial
`01.018.001`, os fingerprints dos dois dumps, as evidências do experimento
patch-only e a working copy validada. O payload atualizado pode ser
reproduzido a partir desses materiais e foi removido para recuperar espaço.

- Decisão e remoção do payload: 21 de novembro de 2026
- Payload removido: árvore `PPSA04610-app0_ELDEN_RING`
- Dados mantidos: este tombstone, `param.json`, `dump-info.json` e os dois
  manifestos completos
