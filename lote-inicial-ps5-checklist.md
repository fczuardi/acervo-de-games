---
layout: post
title: "Checklist de preservação do lote inicial PS5"
date: 2026-11-10 00:00:00 -0300
permalink: /lote-inicial-ps5-checklist/
---

Esta é minha lista de trabalho para levar até o fim a preservação dos oito jogos do [lote inicial de PS5]({% post_url 2026-11-08-lote-inicial-ps5 %}) e de *Recompile*, incorporado depois ao mesmo lote. Cada etapa costuma ocupar pelo menos uma hora, às vezes várias. A ideia desta página é deixar visível o que já foi feito e qual é o próximo trabalho, sem depender da memória ou da empolgação do dia.

Não uso “preservado” aqui como uma afirmação absoluta. Para esta meta, considero concluído o ciclo mínimo quando preservei a instalação limpa do disco, a atualização oficial compatível, os fingerprints dos dois dumps e uma cópia de trabalho que consegui executar sem o disco.

**Progresso obrigatório: 53 de 79 etapas — 67,1%.**

<progress value="53" max="79">53 de 79</progress>

`✅` concluído · `◐` em andamento ou aguardando conferência · `—` ainda não iniciado · `○` opcional · `n/a` não se aplica

| Jogo | Inv. | Dump base | FP base | Manifesto update | PKG | FP PKG | Dump atualizado | FP atualizado | Working copy | FP working |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Demon's Souls (`PPSA01342`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Marvel's Spider-Man: Miles Morales (`PPSA01411`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Ratchet & Clank: Em Uma Outra Dimensão (`PPSA01473`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Elden Ring (`PPSA04610`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Helldivers II (`PPSA01413`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Marvel's Spider-Man 2 (`PPSA03016`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Astro Bot (`PPSA21564`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Death Stranding 2: On the Beach (`PPSA02015`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Recompile (`PPSA03183`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | n/a | n/a | ✅ | ✅ |

## Título digital adicional

My First Gran Turismo não entra no denominador de 79 etapas do lote físico:
não há disco nem uma instalação-base em mídia para preservar. Uso a mesma
tabela para acompanhar o que é comparável; `n/a` indica uma etapa que não se
aplica ao caso digital.

| Jogo | Inv. | Dump base | FP base | Manifesto update | PKG | FP PKG | Dump atualizado | FP atualizado | Working copy | FP working |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| My First Gran Turismo (`PPSA24156`) | n/a | n/a | n/a | ◐ | — | — | ✅ | ✅ | ✅ | ✅ |

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
- **Ratchet & Clank 01.000.000:** o sistema marcou a cópia do disco como concluída embora o PlayGo mostrasse `78% HERE`, indicando que chunks não solicitados de idioma ou região não foram instalados. O dump-base terminou com 71.665.144.695 bytes processados, descriptografia ligada e FSELF/backport desligados. O fingerprint registra 157 arquivos e 71.608.537.575 bytes aparentes; os hashes dos manifestos SHA-256 e de tamanhos são, respectivamente, `6770c3aaaaab6a505a1309190ee712ca11009591c4a76fbd11472c98b1480a12` e `f1b775d128a2ad7ae6cdc05dffc8c8c59288bc9e10ffbc1edbea224c04e544c9`.
- **Ratchet & Clank 01.005.003:** dump atualizado antigo incorporado ao acervo e fingerprint concluído; a versão coincide com o patch preservado, mas a extração não possui `dump-info.json` nem log específico preservado. A working copy FFPKG foi validada, possui 37.576.966.144 bytes e SHA-256 `4cb15dd0f68c2302646eaef9856ef865cdd06a9e2a135d9dadf9b0eff81b2473`. Depois desses controles, o payload atualizado foi substituído por tombstone.
- **Miles Morales 01.012.000:** dump intermediário convertido em tombstone após o fingerprint. A revisão é historicamente distinta e não é reconstruível a partir de `01.015.001`, mas seu payload ficou fora do escopo definido para o acervo; os dois manifestos e metadados essenciais foram preservados.
- **Astro Bot 01.018.000:** dump intermediário convertido em tombstone após o fingerprint. A revisão é historicamente distinta e não é reconstruível a partir de `01.019.000`, mas seu payload ficou fora do escopo definido para o acervo; os dois manifestos e metadados essenciais foram preservados.
- **Marvel's Spider-Man 2 01.004.003:** dump intermediário convertido em tombstone após o fingerprint. A revisão é historicamente distinta e não é reconstruível a partir de `01.005.001`, mas seu payload ficou fora do escopo definido para o acervo; os dois manifestos e metadados essenciais foram preservados.
- **My First Gran Turismo 01.010.000:** dump antigo incorporado ao acervo e fingerprint concluído. O ProsperoPatches identifica esta como a versão mais recente, com firmware mínimo `10.20.00.06`; o manifesto original e o PKG ainda precisam ser preservados. O FFPKG foi executado com sucesso no console, possui 14.807.597.056 bytes e SHA-256 `c2cd23c9f4e67b87948d6be2dde3760574a66f377fb64b5a31eadf21e1e2a8e1`.
- **Recompile 01.005.000:** a edição limitada contém Master Version `02.00` e uma revisão mais nova que o `01.004.000` disponível no histórico público de updates. O dump-base foi concluído e fingerprintado: 176 arquivos e 2.801.195.414 bytes aparentes. A imagem Dump Forge também foi criada, fingerprintada e validada sem o disco durante a primeira missão inteira, sem problemas visíveis. Como o patch preservado é anterior à versão do disco, as etapas de dump atualizado não se aplicam a esta mídia.
- **Elden Ring 01.018.001:** retail PKG de 65.184.595.968 bytes e fingerprint concluídos; o conjunto preservado contém registro de aquisição, SHA-256, checksums agregados e verificação das 17/17 partes contra o manifesto da Sony.
- **Elden Ring 01.018.001 patch-only:** o disco `01.000.000` licenciou a execução da aplicação completa instalada somente a partir do retail update; o jogo chegou normalmente à tela de início. O dump foi concluído com o PS5 App Dumper v2.10. O `dump-info.json` registra estado `done`, 156.112.555.864 bytes processados, descriptografia ligada, FSELF e backport desligados. O fingerprint do dump foi concluído.
- **Elden Ring fingerprints:** o dump patch-only possui 114.735 arquivos e 156.057.680.842 bytes aparentes fora de `sce_sys/`. O fingerprint de 49 arquivos e 75.145.310.275 bytes registra a pasta Zstandard intermediária. O FFPKG definitivo possui 75.301.584.896 bytes e SHA-256 `9f0d5296153750a5eded831310d6511baa00362d262874eda8d32af1702e96a7`.
- **Elden Ring working copy:** depois de duas falhas do Dump Forge no PS5, a versão Linux v0.5.6 produziu uma pasta Zstandard nível 9, posteriormente convertida pela Web UI em FFPKG. O FFPKG foi montado, executado com sucesso no console e fingerprintado; a working copy está concluída. Depois desses controles, o payload atualizado foi substituído por tombstone.
- **Elden Ring 01.000.000:** dump-base antigo incorporado ao acervo e fingerprint concluído; a extração não possui `dump-info.json` nem log específico preservado.
- **Helldivers II 01.007.101:** PKG e fingerprint concluídos. Os dumps base e atualizado e a working copy foram adiados conscientemente por causa da dependência do serviço online e da prioridade de títulos mais autônomos da fila.

## Próximo marco

Preservar o manifesto e o retail PKG de My First Gran Turismo e retomar os demais dumps físicos.

Última atualização: 21 de novembro de 2026.

