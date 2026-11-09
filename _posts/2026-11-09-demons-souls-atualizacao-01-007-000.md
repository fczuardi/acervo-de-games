---
title: "Demon's Souls — preservação da atualização 01.007.000"
date: 2026-11-09 08:26:00 -0300
---

Depois de preservar a instalação limpa do disco físico de Demon's Souls, na versão `01.000.000`, fui atrás da atualização mais recente compatível com meu PS5 no firmware 13.60.

Encontrei a versão `01.007.000` no ProsperoPatches e baixei o PKG retail original da Sony com o `fetchpkg` no Linux, sem autenticação na PSN. O pacote veio dividido em 14 partes, todas verificadas com sucesso pelos hashes SHA-256 do manifesto da Sony.

O arquivo montado tem 53.805.318.144 bytes e SHA-256:

```
af8f4e109085b6e28ed53c9af6b23295443edc965aa095e7637770cf0e63b523
```

Esse hash não é igual ao campo `packageDigest` do manifesto. Ainda não determinei o significado exato desse campo.

## Instalação offline

Transferi o PKG para o PS5, mantido offline. O PS5 Web File Manager reconheceu o pacote e permitiu instalá-lo pelo mecanismo nativo do console.

A atualização foi aplicada diretamente sobre a instalação-base `01.000.000`, sem instalar versões intermediárias. O processo terminou com a notificação **Updated**.

Depois da instalação, a interface do PS5 informou:

- versão instalada: `01.007.000`;
- status do download: Completed;
- local da instalação: armazenamento do console;
- tamanho instalado: 53,85 GB.

O jogo abriu normalmente e chegou até a tela de seleção de idioma. Isso confirma apenas a inicialização: não fiz uma verificação completa de jogabilidade.

## Dump da versão atualizada

Em seguida, fiz um novo dump com o PS5 App Dumper v2.10, usando as mesmas configurações do [protocolo de preservação v0.3.0](https://fczuardi.github.io/acervo-de-games/2026/11/08/dump-de-referencia-base-v1.html).

O `dump.log` registra o modo `FLAT`, a conclusão da cópia e a descriptografia bem-sucedida dos executáveis. O processo levou aproximadamente **2h07**.

- Jogo: Demon's Souls
- Title ID: `PPSA01342`
- Content ID: `UP9000-PPSA01342_00-DEMONSSOULS00000`
- Versão: `01.007.000`
- Versão de origem indicada em `param.json`: `01.000.000`
- Firmware mínimo indicado em `param.json`: `12.02`
- Pasta: `PPSA01342-app0_Demon's_Souls`
- Modo de extração: `FLAT`
- Arquivos: 223.266
- Tamanho aparente: 88.040.155.281 bytes
- Bytes reportados pelo dumper: 88.025.095.888

## Integridade

Os manifestos excluem `sce_sys/`, seguindo o protocolo publicado.

- Arquivos incluídos: 223.238
- Arquivos excluídos: 28
- Manifesto SHA-256: `PPSA01342-01.007.000.sha256`
- Manifesto de tamanhos: `PPSA01342-01.007.000.sizes.tsv`

**SHA-256 do manifesto de arquivos:**

```
f78516ad791e595fddc6ca6cab25c9a75dbf496a360cf1f5fa38a209431a88fb
```

**SHA-256 do manifesto de tamanhos:**

```
b6a6d48b3adde38ee81dbecd465f83dcb38784c932976d3f21a7175aaf81b58e
```

**SHA-256 do `eboot.bin` descriptografado:**

```
4a6ca8a2904d02a9ff11aebcb10379c89974cd9bff1a37e09c21a7e782447674
```

## Metadados do dumper

O arquivo `PPSA01342-app0_Demon's_Souls.dump-info.json` contém os seguintes dados, com os campos `started` e `finished` omitidos por serem específicos desta execução:

```json
{
  "tool": "ps5-app-dumper",
  "version": "2.10",
  "titleId": "PPSA01342",
  "title": "Demon's Souls",
  "folder": "PPSA01342-app0_Demon's_Souls",
  "state": "done",
  "bytes": 88025095888,
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

Preservei separadamente o PKG retail original, o manifesto de distribuição da Sony e o dump descriptografado. Nenhum desses arquivos de jogo é publicado aqui; este registro contém apenas metadados, observações e hashes.

#ps5 #demons-souls #atualizacao #dump #preservacao
