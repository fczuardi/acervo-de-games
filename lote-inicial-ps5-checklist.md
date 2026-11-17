---
layout: post
title: "Checklist de preservação do lote inicial PS5"
date: 2026-11-10 00:00:00 -0300
permalink: /lote-inicial-ps5-checklist/
---

Esta é minha lista de trabalho para levar até o fim a preservação dos oito jogos do [lote inicial de PS5]({% post_url 2026-11-08-lote-inicial-ps5 %}). Cada etapa costuma ocupar pelo menos uma hora, às vezes várias. A ideia desta página é deixar visível o que já foi feito e qual é o próximo trabalho, sem depender da memória ou da empolgação do dia.

Não uso “preservado” aqui como uma afirmação absoluta. Para esta meta, considero concluído o ciclo mínimo quando preservei a instalação limpa do disco, a atualização oficial compatível, os fingerprints dos dois dumps e uma cópia de trabalho que consegui executar sem o disco.

**Progresso obrigatório: 37 de 72 etapas — 51,4%.**

<progress value="37" max="72">37 de 72</progress>

`✅` concluído · `◐` em andamento ou aguardando conferência · `—` ainda não iniciado · `○` opcional

| Jogo | Inv. | Dump base | FP base | Manifesto update | PKG | FP PKG | Dump atualizado | FP atualizado | Working copy | FP working |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Demon's Souls (`PPSA01342`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Marvel's Spider-Man: Miles Morales (`PPSA01411`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Ratchet & Clank: Em Uma Outra Dimensão (`PPSA01473`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Elden Ring (`PPSA04610`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Helldivers II (`PPSA01413`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Marvel's Spider-Man 2 (`PPSA03016`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Astro Bot (`PPSA21564`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Death Stranding 2: On the Beach (`PPSA02015`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |

## O que cada coluna quer dizer

- **Inv.**: mídia física identificada no inventário, com os dados visíveis da embalagem e do disco.
- **Dump base**: instalação limpa do disco, sem update, extraída de acordo com o protocolo vigente.
- **FP base**: manifestos SHA-256 e de tamanhos do dump base, com seus próprios hashes registrados.
- **Manifesto update**: versão mais recente compatível com o firmware `13.60` identificada e manifesto original da Sony preservado.
- **PKG**: retail PKG montado a partir das partes originais e guardado separadamente.
- **FP PKG**: tamanho e SHA-256 do PKG, verificação das partes e registro mínimo da aquisição.
- **Dump atualizado**: update instalado sobre a base e nova versão extraída com o mesmo protocolo.
- **FP atualizado**: manifestos SHA-256 e de tamanhos do dump atualizado, com seus próprios hashes registrados.
- **Working copy**: cópia derivada criada sem alterar o dump de referência, montada e testada sem o disco. O teste deve incluir pelo menos início do jogo, algum tempo de jogo e, quando aplicável, salvar e retomar.
- **FP working**: hash da imagem de trabalho final. É útil, mas opcional: ela pode ser recriada a partir do dump preservado e das anotações.

## Estado das tarefas em andamento

- **Demon's Souls 01.007.000:** fingerprint SHA-256 da imagem de trabalho final concluído. O payload do dump atualizado foi convertido em tombstone após a comparação com o dump patch-only demonstrar conteúdo idêntico fora de `sce_sys/`; os manifestos, metadados e logs foram preservados.
- **Death Stranding 2 01.015.000:** PKG e fingerprint concluídos; as 23 partes do manifesto foram verificadas e o conjunto de preservação foi finalizado.
- **Marvel's Spider-Man 2 01.005.001:** PKG e fingerprint concluídos; as 27 partes do manifesto foram verificadas e o conjunto de preservação foi finalizado.
- **Elden Ring 01.018.001:** PKG e fingerprint concluídos; o conjunto preservado contém registro de aquisição, verificação por partes e checksums agregados.
- **Helldivers II 01.007.101:** PKG e fingerprint concluídos. Os dumps base e atualizado e a working copy foram adiados conscientemente por causa da dependência do serviço online e da prioridade de títulos mais autônomos da fila.

## Próximo marco

Retomar no PS5 os dumps base e atualizado dos títulos físicos, priorizando jogos autônomos que possam ser testados offline.

Última atualização: 18 de novembro de 2026.

