---
layout: post
title: "Checklist de preservação do lote inicial PS5"
date: 2026-11-10 00:00:00 -0300
permalink: /lote-inicial-ps5-checklist/
---

Esta é minha lista de trabalho para levar até o fim a preservação dos oito jogos do [lote inicial de PS5]({% post_url 2026-11-08-lote-inicial-ps5 %}) e de *Recompile*, incorporado depois ao mesmo lote. Cada etapa costuma ocupar pelo menos uma hora, às vezes várias. A ideia desta página é deixar visível o que já foi feito e qual é o próximo trabalho, sem depender da memória ou da empolgação do dia.

Não uso “preservado” aqui como uma afirmação absoluta. Para esta meta, considero concluído o ciclo mínimo quando preservei a instalação limpa do disco, a atualização oficial compatível, os fingerprints dos dois dumps e uma cópia de trabalho que consegui executar sem o disco.

**Progresso obrigatório: 74 de 79 etapas — 93,7%.**

<progress value="74" max="79">74 de 79</progress>

`✅` concluído · `◐` em andamento ou aguardando conferência · `—` ainda não iniciado · `○` opcional · `n/a` não se aplica

| Jogo | Inv. | Dump base | FP base | Manifesto update | PKG | FP PKG | Dump atualizado | FP atualizado | Working copy | FP working |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Demon's Souls (`PPSA01342`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Marvel's Spider-Man: Miles Morales (`PPSA01411`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ratchet & Clank: Em Uma Outra Dimensão (`PPSA01473`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Elden Ring (`PPSA04610`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Helldivers II (`PPSA01413`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Marvel's Spider-Man 2 (`PPSA03016`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Astro Bot (`PPSA21564`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Death Stranding 2: On the Beach (`PPSA02015`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Recompile (`PPSA03183`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | n/a | n/a | ✅ | ✅ |

## Títulos digitais adicionais

My First Gran Turismo e ASTRO's PLAYROOM não entram no denominador de 79
etapas do lote físico: não há disco nem uma instalação-base em mídia para
preservar. Uso a mesma tabela para acompanhar o que é comparável; `n/a` indica
uma etapa que não se aplica ao caso digital. Como não existe disco para
reconstruí-los, o dump integral limpo desses títulos não deve virar tombstone
sem prova de reconstrução contra seu fingerprint ou outra fonte integral
independente.

| Jogo | Inv. | Dump base | FP base | Manifesto update | PKG | FP PKG | Dump atualizado | FP atualizado | Working copy | FP working |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| My First Gran Turismo (`PPSA24156`) | n/a | n/a | n/a | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| ASTRO's PLAYROOM (`PPSA01325`) | n/a | n/a | n/a | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

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
- **Death Stranding 2 dumps:** a base `01.000.000` e a versão atualizada `01.015.000` foram extraídas com o PS5 App Dumper v2.10. Os sidecars registram estado `done`, respectivamente 170.366.093.246 e 170.212.860.783 bytes processados, descriptografia ligada e FSELF/backport desligados. O fingerprint-base contém 222 arquivos e 170.317.716.329 bytes aparentes; os hashes dos manifestos SHA-256 e de tamanhos são `54518b0e5573ba7827aa999619ce12ed673c547e632ca90729ccf545de81d199` e `af2b555eed617556fde1b2e53a5a40a1ed27f219d70656da3d6a0c0cce8cf9f4`. O atualizado contém 231 arquivos e 170.164.452.683 bytes aparentes; os hashes são `cbe1893ff3e15819daed46c3cf255eefe86cc43a7bf357ddb5e0d0ddfc9d12f2` e `d0c79c57734f918309c763e3bbbcbc3d9ed81a96d0bc926e1df1cbb977b5fe02`.
- **Death Stranding 2 working copy:** o Dump Forge v0.5.7 produziu uma FFPKG Zstandard de 101.272.584.192 bytes, versão `01.015.000`, sem achados na verificação completa. O SHA-256 `f2f8612d9a7a0b9a9cd773563331c8a8503c7f61dec714f0415f53e189e6cf21` foi conferido novamente depois da cópia para o HD. A imagem foi copiada para o M.2, montada e executada sem o disco no console. Com o disco e o retail patch como fontes recuperáveis, os payloads dos dumps base e atualizado foram substituídos por tombstones.
- **Marvel's Spider-Man 2 dumps:** a base `01.000.000` e a versão atualizada `01.005.001` foram extraídas com o PS5 App Dumper v2.10. Os sidecars registram estado `done`, respectivamente 240.442.658.435 e 272.607.329.443 bytes processados, descriptografia ligada e FSELF/backport desligados. O fingerprint-base contém 226 arquivos e 240.388.963.575 bytes aparentes; os hashes dos manifestos SHA-256 e de tamanhos são `841a819abce203334d1e20be75ee05d7c73080db8fec25d5058f30f1bd0fba14` e `f4925ba1c7c332a02b2175dea682560781098ec9ea0011d5f8d802d36d0e1e09`. O atualizado contém 236 arquivos e 272.553.451.132 bytes aparentes; os hashes são `7f4eda9eda9f9c3d29410863b2aa748a8b1f73b79b7ad7d47a2b527b0d06ec7f` e `6ca1b253e54bb3cc7307bf2e643eb726a8110abaf13b913a7f5ac90269485836`.
- **Marvel's Spider-Man 2 working copy:** o Dump Forge v0.5.7 produziu uma FFPKG Zstandard de 121.943.162.880 bytes, versão `01.005.001`, sem achados na verificação completa. O SHA-256 `a03a3815086d92ad631d4e9acb5f9c39206211cbf68ad5715755f4ad4ba3d620` foi conferido novamente depois da cópia para o HD. A imagem foi copiada para o M.2, montada e executada sem o disco no console. Com o disco e o retail patch como fontes recuperáveis, os payloads dos dumps base e atualizado foram substituídos por tombstones.
- **Miles Morales 01.015.001:** dump atualizado concluído com o PS5 App Dumper v2.10, estado `done`, 95.028.895.196 bytes processados, descriptografia ligada e FSELF/backport desligados. O fingerprint registra 162 arquivos e 94.977.107.680 bytes aparentes; os hashes dos manifestos SHA-256 e de tamanhos são `b4cc61d3cc1e192de05c26010bdf347400dab17d59fc721a501b6218d930abb6` e `541e80550d87ed89d1220f29982959062fe0fa3ce25a15791546e907154053c0`.
- **Miles Morales working copy:** a FFPKG `01.015.001` possui 55.416.848.384 bytes e SHA-256 `0b21779744186e60bc0abb13fcba02990a55d8681cac7149cc135ff0ab6d23ce`; depois da criação e do fingerprint, a imagem foi copiada para o M.2, montada e executada sem o disco no console. Com o dump-base `01.000.000`, o retail patch e a working image preservados, o payload do dump atualizado `01.015.001` foi substituído por tombstone.
- **Ratchet & Clank 01.000.000:** o sistema marcou a cópia do disco como concluída embora o PlayGo mostrasse `78% HERE`, indicando que chunks não solicitados de idioma ou região não foram instalados. O dump-base terminou com 71.665.144.695 bytes processados, descriptografia ligada e FSELF/backport desligados. O fingerprint registra 157 arquivos e 71.608.537.575 bytes aparentes; os hashes dos manifestos SHA-256 e de tamanhos são, respectivamente, `6770c3aaaaab6a505a1309190ee712ca11009591c4a76fbd11472c98b1480a12` e `f1b775d128a2ad7ae6cdc05dffc8c8c59288bc9e10ffbc1edbea224c04e544c9`.
- **Ratchet & Clank 01.005.003:** dump atualizado antigo incorporado ao acervo e fingerprint concluído; a versão coincide com o patch preservado, mas a extração não possui `dump-info.json` nem log específico preservado. A working copy FFPKG foi validada, possui 37.576.966.144 bytes e SHA-256 `4cb15dd0f68c2302646eaef9856ef865cdd06a9e2a135d9dadf9b0eff81b2473`. Depois desses controles, o payload atualizado foi substituído por tombstone.
- **Miles Morales 01.012.000:** dump intermediário convertido em tombstone após o fingerprint. A revisão é historicamente distinta e não é reconstruível a partir de `01.015.001`, mas seu payload ficou fora do escopo definido para o acervo; os dois manifestos e metadados essenciais foram preservados.
- **Astro Bot 01.018.000:** dump intermediário convertido em tombstone após o fingerprint. A revisão é historicamente distinta e não é reconstruível a partir de `01.019.000`, mas seu payload ficou fora do escopo definido para o acervo; os dois manifestos e metadados essenciais foram preservados.
- **Astro Bot 01.019.000 patch-only:** segunda aplicação do protocolo experimental v0.4.0 concluída. O retail update foi instalado sem base; `/user/app/PPSA21564` e `appmeta` ficaram presentes, `/user/patch/PPSA21564` permaneceu ausente e o disco licenciou a execução. O dump atualizado terminou com o PS5 App Dumper v2.10 e seu fingerprint registra 166.700 arquivos e 159.744.132.637 bytes aparentes. A working copy FFPKG Zstandard foi verificada e executada sem o disco; possui 45.609.320.448 bytes e SHA-256 `73b2cacf3dff4631f45c7b4e1cbf74182b93643259e525bdfe5c77f3f56887c9`. Depois desses controles, o payload atualizado foi substituído por tombstone.
- **Astro Bot 01.000.000:** instalação limpa do disco extraída com estado `done`, 154.993.980.216 bytes processados, descriptografia ligada e FSELF/backport desligados. O fingerprint registra 146.987 arquivos e 154.935.393.869 bytes aparentes. Com o dump-base e a working copy validados, todas as etapas obrigatórias do título estão concluídas.
- **Miles Morales 01.000.000:** dump-base concluído com o PS5 App Dumper v2.10, estado `done`, 78.759.017.680 bytes processados, descriptografia ligada e FSELF/backport desligados. O fingerprint registra 162 arquivos e 78.707.202.405 bytes aparentes; os hashes dos manifestos SHA-256 e de tamanhos são `aefa3df2f515c31ca4c16121f1b7fbdd854527b2bb8fb5b7b47ff703cd700bd2` e `03fd4ec37a6b8b67d514cccc090cb18efc8febe8d317b10142b2dedd8e06329b`.
- **Marvel's Spider-Man 2 01.004.003:** dump intermediário convertido em tombstone após o fingerprint. A revisão é historicamente distinta e não é reconstruível a partir de `01.005.001`, mas seu payload ficou fora do escopo definido para o acervo; os dois manifestos e metadados essenciais foram preservados.
- **My First Gran Turismo 01.010.000:** dump antigo incorporado ao acervo e fingerprint concluído. O retail PKG oficial possui 13.099.401.216 bytes e SHA-256 `7a8db7f03603a55529410b158d0733c0f9492352164332e8a9b933bfaca94a11`; as cinco partes do manifesto Sony conferiram. O FFPKG foi executado com sucesso no console, possui 14.807.597.056 bytes e SHA-256 `c2cd23c9f4e67b87948d6be2dde3760574a66f377fb64b5a31eadf21e1e2a8e1`. Todas as etapas aplicáveis estão concluídas e o payload do dump foi substituído por tombstone, mantendo os manifestos e o sidecar. Como este era o único dump integral de um título digital-only, ficou registrado que futuros casos assim exigem confirmação específica ou prova de reconstrução da working copy contra o fingerprint antes do descarte.
- **ASTRO's PLAYROOM 01.905.000:** incorporado como segundo título digital adicional. O manifesto oficial identifica quatro partes, 11.709.579.264 bytes e `packageDigest` `026F3814C2DF678094E1AEB6E4FEA23CC6D5E261AEAAF54B37CCF564B6975AF1`. As quatro faixas conferiram com os hashes SHA-256 declarados pela Sony, sem gaps, overlaps ou mismatches; o PKG integral possui SHA-256 `47a755b651c17aa6925d577223401b97c6f06d5287b29a31e8f8c7135572574b`. A instalação via PatchDL funcionou e o novo dump terminou com o PS5 App Dumper v2.10 em estado `done`, 29.614.140.157 bytes processados, descriptografia ligada e FSELF/backport desligados. O fingerprint registra 34.357 arquivos e 29.559.790.545 bytes aparentes; os hashes dos manifestos SHA-256 e de tamanhos são `593ab37efa87aeb896461fb437fa739d4d1e4ba4ce99326e0022ad809d509617` e `63669343a11b52892529e452221196d852ddce03a7e002d0650993dc06a583fd`. O Dump Forge v0.5.7 produziu uma FFPKG Zstandard de 12.973.113.344 bytes, sem achados na verificação completa, com SHA-256 `75421702ec51fe0e6944da152cf5e9d20388d134290c4b0d4cba48cac6390104`; a imagem foi montada e executada sem o disco no console. O dump integral limpo permanece preservado por se tratar de um título digital. O dump antigo em `/archive`, que contém modificações como `fakelib`, não substitui esse novo material.
- **Recompile 01.005.000:** a edição limitada contém Master Version `02.00` e uma revisão mais nova que o `01.004.000` disponível no histórico público de updates. O dump-base foi concluído e fingerprintado: 176 arquivos e 2.801.195.414 bytes aparentes. A imagem Dump Forge também foi criada, fingerprintada e validada sem o disco durante a primeira missão inteira, sem problemas visíveis. Como o patch preservado é anterior à versão do disco, as etapas de dump atualizado não se aplicam a esta mídia.
- **Elden Ring 01.018.001:** retail PKG de 65.184.595.968 bytes e fingerprint concluídos; o conjunto preservado contém registro de aquisição, SHA-256, checksums agregados e verificação das 17/17 partes contra o manifesto da Sony.
- **Elden Ring 01.018.001 patch-only:** o disco `01.000.000` licenciou a execução da aplicação completa instalada somente a partir do retail update; o jogo chegou normalmente à tela de início. O dump foi concluído com o PS5 App Dumper v2.10. O `dump-info.json` registra estado `done`, 156.112.555.864 bytes processados, descriptografia ligada, FSELF e backport desligados. O fingerprint do dump foi concluído.
- **Elden Ring fingerprints:** o dump patch-only possui 114.735 arquivos e 156.057.680.842 bytes aparentes fora de `sce_sys/`. O fingerprint de 49 arquivos e 75.145.310.275 bytes registra a pasta Zstandard intermediária. O FFPKG definitivo possui 75.301.584.896 bytes e SHA-256 `9f0d5296153750a5eded831310d6511baa00362d262874eda8d32af1702e96a7`.
- **Elden Ring working copy:** depois de duas falhas do Dump Forge no PS5, a versão Linux v0.5.6 produziu uma pasta Zstandard nível 9, posteriormente convertida pela Web UI em FFPKG. O FFPKG foi montado, executado com sucesso no console e fingerprintado; a working copy está concluída. Depois desses controles, o payload atualizado foi substituído por tombstone.
- **Elden Ring 01.000.000:** dump-base antigo incorporado ao acervo e fingerprint concluído; a extração não possui `dump-info.json` nem log específico preservado.
- **Helldivers II 01.007.101:** PKG e fingerprint concluídos. Os dumps base e atualizado e a working copy foram adiados conscientemente por causa da dependência do serviço online e da prioridade de títulos mais autônomos da fila.

## Próximo marco

O único bloco ainda incompleto é Helldivers II, conscientemente adiado por sua
dependência online. Os dois títulos digitais adicionais também concluíram todas
as etapas aplicáveis.

Última atualização: 23 de novembro de 2026.

