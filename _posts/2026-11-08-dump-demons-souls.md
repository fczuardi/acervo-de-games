---
title: "Demon's Souls — primeiro dump de referência"
date: 2026-11-08 21:34:00 -0300
---

Hoje fiz um novo dump do disco físico de Demon's Souls para PS5 (PPSA01342), seguindo o [protocolo de referência v0.2.1](https://fczuardi.github.io/acervo-de-games/2026/11/08/dump-de-referencia-base-v1.html).

A intenção foi preservar os arquivos da versão original do disco, sem atualizações baixadas pela internet e sem modificações para execução via homebrew.

## Procedimento

Usei meu PS5 com firmware 13.60 e o PS5 App Dumper v2.10 beta, com descriptografia de executáveis ativada, FSELF e SDK backport desativados.

Removi a instalação anterior, mantive o console offline, instalei o jogo a partir do disco e aguardei a conclusão da cópia antes de executar o dumper.

O processo de dump levou aproximadamente **1h52**, terminando com sucesso, incluindo a descriptografia dos executáveis.

## Resultado

- Jogo: Demon's Souls
- Title ID: `PPSA01342`
- Content ID: `UP9000-PPSA01342_00-DEMONSSOULS00000`
- Versão instalada: `01.000.000`
- Pasta: `PPSA01342-app0_Demon's_Souls`
- Modo de extração: `FLAT`
- Arquivos: 222.936
- Tamanho aparente: 87.399.836.759 bytes
- Bytes reportados pelo dumper: 87.384.786.240

A cópia foi armazenada em uma unidade exFAT com clusters de 128 KiB. Embora os arquivos representem aproximadamente 87,4 GB, o diretório ocupa cerca de 106 GiB no disco, devido principalmente ao espaço de alocação desperdiçado pelos muitos arquivos pequenos.

## Integridade

Gerei um manifesto SHA-256 dos arquivos regulares do dump, excluindo `sce_sys/`, que contém metadados parcialmente copiados de áreas do sistema do PS5.

- Arquivos incluídos: 222.912
- Arquivos excluídos: 24
- Manifesto: `PPSA01342-base.sha256`
- Tamanho do manifesto: aproximadamente 34 MB

**SHA-256 do manifesto:**

```
1febf4d9305e743cafc429dc47b2dbb157449692336a8bdce27d42b1e486d866
```

**SHA-256 do `eboot.bin` descriptografado:**

```
7684034de92b7282a946e4d80acecac2206a791812fa6dbdeadec031bc4b557a
```

O executável foi identificado pelo Linux como ELF de 64 bits, x86-64, ABI FreeBSD.

O manifesto registra os hashes calculados após o dump e poderá ser utilizado para verificações de integridade posteriores.

## Metadados do dumper

O PS5 App Dumper gerou o arquivo `PPSA01342-app0_Demon's_Souls.dump-info.json`.

Conteúdo original, exceto pelos campos `started` e `finished`, removidos por serem específicos desta execução:

```json
{
  "tool": "ps5-app-dumper",
  "version": "2.10",
  "titleId": "PPSA01342",
  "title": "Demon's Souls",
  "folder": "PPSA01342-app0_Demon's_Souls",
  "state": "done",
  "bytes": 87384786240,
  "settings": {
    "decrypt": 1,
    "fself": 0,
    "backport": 0,
    "ps4BackportLevel": 4,
    "ps5BackportLevel": 1,
    "split": 3
  }
}
```

## Comparação com um dump anterior

Encontrei outro dump de Demon's Souls, realizado em 20 de outubro de 2026, aparentemente com as mesmas configurações.

Inicialmente os executáveis pareciam inconsistentes: o `eboot.bin` anterior tinha 48.078.428 bytes e um SHA-256 diferente:

```
3f8aa1064e082ef0020ec404aa23c75f22a1750a86a689d219653c73227483f9
```

A comparação dos arquivos `sce_sys/param.json` revelou que o dump anterior era da versão `01.004.000`, enquanto o novo é da versão `01.000.000`.

Portanto, não se trata de duas extrações da mesma versão. Essa diferença explica de maneira plausível as alterações no executável, mas ainda não demonstra a reprodutibilidade do dumper.

O dump antigo foi preservado.

## Próximos passos

Pretendo preservar também a última atualização compatível com o firmware 13.60, atualmente identificada como `01.007.000`, e testar sua instalação offline.

Os arquivos dos jogos e os pacotes de atualização não são disponibilizados neste repositório. Os registros públicos contêm apenas metadados, procedimentos e hashes.

#ps5 #demons-souls #dump #preservacao
