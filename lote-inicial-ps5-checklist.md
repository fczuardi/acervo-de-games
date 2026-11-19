---
layout: post
title: "Checklist de preservação do lote inicial PS5"
date: 2026-11-10 00:00:00 -0300
permalink: /lote-inicial-ps5-checklist/
---

Esta é minha lista de trabalho para levar até o fim a preservação dos oito jogos do [lote inicial de PS5]({% post_url 2026-11-08-lote-inicial-ps5 %}) e de *Recompile*, incorporado depois ao mesmo lote. Cada etapa costuma ocupar pelo menos uma hora, às vezes várias. A ideia desta página é deixar visível o que já foi feito e qual é o próximo trabalho, sem depender da memória ou da empolgação do dia.

Não uso “preservado” aqui como uma afirmação absoluta. Para esta meta, considero concluído o ciclo mínimo quando preservei a instalação limpa do disco, a atualização oficial compatível, os fingerprints dos dois dumps e uma cópia de trabalho que consegui executar sem o disco.

**Progresso obrigatório: 45 de 81 etapas — 55,6%.**

<progress value="45" max="81">45 de 81</progress>

`✅` concluído · `◐` em andamento ou aguardando conferência · `—` ainda não iniciado · `○` opcional

| Jogo | Inv. | Dump base | FP base | Manifesto update | PKG | FP PKG | Dump atualizado | FP atualizado | Working copy | FP working |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Demon's Souls (`PPSA01342`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Marvel's Spider-Man: Miles Morales (`PPSA01411`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Ratchet & Clank: Em Uma Outra Dimensão (`PPSA01473`) | ✅ | — | — | ✅ | ✅ | ✅ | ✅ | ✅ | — | ○ |
| Elden Ring (`PPSA04610`) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | — | — | — | ○ |
| Helldivers II (`PPSA01413`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Marvel's Spider-Man 2 (`PPSA03016`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Astro Bot (`PPSA21564`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Death Stranding 2: On the Beach (`PPSA02015`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |
| Recompile (`PPSA03183`) | ✅ | — | — | ✅ | ✅ | ✅ | — | — | — | ○ |

## Título digital adicional

My First Gran Turismo não entra no denominador de 72 etapas do lote físico:
não há disco nem uma instalação-base em mídia para preservar. Uso a mesma
tabela para acompanhar o que é comparável; `n/a` indica uma etapa que não se
aplica ao caso digital.

| Jogo | Inv. | Dump base | FP base | Manifesto update | PKG | FP PKG | Dump atualizado | FP atualizado | Working copy | FP working |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| My First Gran Turismo (`PPSA24156`) | n/a | n/a | n/a | ◐ | — | — | ✅ | ✅ | — | ○ |

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
- **Ratchet & Clank 01.005.003:** dump atualizado antigo incorporado ao acervo e fingerprint concluído; a versão coincide com o patch preservado, mas a extração não possui `dump-info.json` nem log específico preservado.
- **Miles Morales 01.012.000:** dump intermediário convertido em tombstone após o fingerprint. A revisão é historicamente distinta e não é reconstruível a partir de `01.015.001`, mas seu payload ficou fora do escopo definido para o acervo; os dois manifestos e metadados essenciais foram preservados.
- **Astro Bot 01.018.000:** dump intermediário convertido em tombstone após o fingerprint. A revisão é historicamente distinta e não é reconstruível a partir de `01.019.000`, mas seu payload ficou fora do escopo definido para o acervo; os dois manifestos e metadados essenciais foram preservados.
- **Marvel's Spider-Man 2 01.004.003:** dump intermediário convertido em tombstone após o fingerprint. A revisão é historicamente distinta e não é reconstruível a partir de `01.005.001`, mas seu payload ficou fora do escopo definido para o acervo; os dois manifestos e metadados essenciais foram preservados.
- **My First Gran Turismo 01.010.000:** dump antigo incorporado ao acervo e fingerprint concluído. O ProsperoPatches identifica esta como a versão mais recente, com firmware mínimo `10.20.00.06`; o manifesto original e o PKG ainda precisam ser preservados, e a execução offline ainda não foi testada.
- **Recompile 01.004.000:** manifesto, retail PKG e fingerprint concluídos; as duas partes foram verificadas e o conjunto de preservação foi finalizado. O disco ainda não foi inserido no console, preservando o estado inicial para o teste patch-only e a primeira validação da licença física.
- **Elden Ring 01.018.001:** retail PKG de 65.184.595.968 bytes e fingerprint concluídos; o conjunto preservado contém registro de aquisição, SHA-256, checksums agregados e verificação das 17/17 partes contra o manifesto da Sony.
- **Elden Ring 01.000.000:** dump-base antigo incorporado ao acervo e fingerprint concluído; a extração não possui `dump-info.json` nem log específico preservado.
- **Helldivers II 01.007.101:** PKG e fingerprint concluídos. Os dumps base e atualizado e a working copy foram adiados conscientemente por causa da dependência do serviço online e da prioridade de títulos mais autônomos da fila.

## Próximo marco

Executar o teste patch-only de Recompile antes de inserir o disco pela primeira vez; depois criar o dump e a working copy da instalação resultante. Em seguida, criar e testar offline a working copy de My First Gran Turismo e retomar os demais dumps físicos.

Última atualização: 19 de novembro de 2026.

