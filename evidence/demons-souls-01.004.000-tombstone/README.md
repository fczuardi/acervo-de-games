# Tombstone — Demon's Souls 01.004.000

Registro do dump descriptografado intermediário de *Demon's Souls* para PS5
que foi selecionado para descarte por economia de espaço.

## Identificação

- Jogo: Demon's Souls
- Title ID: `PPSA01342`
- Versão observada em `sce_sys/param.json`: `01.004.000`
- Versão-alvo observada em `sce_sys/param.json`: `01.003.000`
- Content ID: `UP9000-PPSA01342_00-DEMONSSOULS00000`
- Firmware mínimo codificado: `0x0226000000000000`
- Início do dump: 20 de outubro de 2026, 16:23:59 -03:00
- Fim do dump: 20 de outubro de 2026, 17:55:22 -03:00
- Ferramenta: PS5 App Dumper v2.10
- Estado registrado pelo dumper: `done`
- Bytes reportados pelo dumper: 88.020.163.452
- Arquivos regulares no manifesto, excluindo `sce_sys/`: 223.214
- Tamanho aparente no manifesto, excluindo `sce_sys/`: 87.951.090.866 bytes
- Opções: descriptografia ligada; FSELF e backport desligados; `split=3`
- `eboot.bin`: 48.078.428 bytes
- SHA-256 do `eboot.bin` descriptografado:
  `3f8aa1064e082ef0020ec404aa23c75f22a1750a86a689d219653c73227483f9`

## Evidência disponível

Antes do descarte, o diretório foi localizado em
`/run/media/fcz/PS5_DUMPS/Acervo/dumps/Demon's Souls - 01.004.000 - PPSA01342`
e os metadados e o executável foram conferidos diretamente. O `param.json`
confirmou `contentVersion` igual a `01.004.000`, e o hash do `eboot.bin`
coincidiu com o registro anterior.

O dump havia sido identificado como `01.004.000` durante a comparação com uma
nova extração da versão de disco `01.000.000`, realizada em 8 de novembro de 2026.
O registro contemporâneo está em
[`_posts/2026-11-08-dump-demons-souls.md`](../../_posts/2026-11-08-dump-demons-souls.md).

Foram preservados neste diretório uma cópia byte a byte de `dump-info.json` e o
conteúdo normalizado de `gameversion.txt` (`BuildVersion=2020-12-09.781263`). O
`param.json` original continha uma URL de distribuição e não foi publicado, mas
teve seus campos principais transcritos acima e seu hash registrado antes do
descarte:

- `dump-info.json`: `1142409043f58f7ef9c58db4de12c826c5fe11b621039a88df7fa0ea0f938179`
- `sce_sys/param.json`: `1a0c31bcd0466e6c5c07609e4e6bb9234af9a7880391a324a74e1e830576ad71`
- `gameversion.txt` original: `e04f3d89c0ad56d99f3676b2304571b45ec17cd9cea5327ef69917d8fadacf93`
- `gameversion.txt` normalizado preservado: `9ea55fcd0aee27808197f59a1cbf995c19faef6169e2ccc1e0eb1a58a1b88599`

Antes do descarte foram gerados manifestos completos dos arquivos regulares,
excluindo `sce_sys/` conforme o protocolo da coleção:

- `PPSA01342-01.004.000.sha256`: 223.214 entradas; SHA-256
  `58384ab2109c6d7b1b38fec6a5dec034a10875d35ddafdf94af30b00303dc801`
- `PPSA01342-01.004.000.sizes.tsv`: 223.214 entradas; SHA-256
  `3bdc6884153d77487a8b0f1094099286755612fc51e984fedf7544362e1a8ab3`

Esses manifestos permitem comparações exatas de caminhos, tamanhos e conteúdo
com outras extrações. Eles não permitem reconstruir os arquivos descartados.

## Motivo do descarte

A coleção mantém a versão-base de disco `01.000.000` e a versão `01.007.000`,
além do PKG retail oficial desta última. A versão `01.007.000` foi instalada e
testada, inclusive sem os arquivos da instalação-base presentes. Para o
objetivo operacional da coleção, `01.004.000` passou a ser redundante, embora
continue sendo uma revisão historicamente distinta e não reconstruível a
partir das versões mantidas.

## Disposição

- Decisão de descarte registrada em: 11 de novembro de 2026
- Payload de jogo: selecionado para descarte; a exclusão não foi executada nem
  verificada a partir deste repositório
- Dados mantidos: este tombstone, os dois manifestos completos e o registro
  público de 8 de novembro de 2026
- Tombstone na mídia de arquivo:
  `/run/media/fcz/PS5_DUMPS/Acervo/dumps/_tombstones/Demon's Souls - 01.004.000 - PPSA01342`

Quando a exclusão do payload for confirmada, este campo deve ser atualizado com
a data e, se possível, o caminho ou identificador da mídia de onde ele foi
removido.
