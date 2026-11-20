---
title: "Elden Ring — protocolo experimental patch-first"
date: 2026-11-20 18:05:00 -0300
---

*Elden Ring* para PS5 (`PPSA04610`) será o primeiro teste completo de uma possível nova versão do protocolo de preservação. Em vez de começar pela instalação limpa do disco e depois aplicar o update, a ordem experimental começa pelo retail patch mais recente compatível, tenta executá-lo sozinho usando o disco apenas como licença e deixa o dump da versão-base para o fim.

Essa ordem aproveita uma propriedade já demonstrada com *Demon's Souls*: certos retail update PKGs de PS5 contêm uma aplicação completa, podem ser instalados sem uma base presente e, quando a versão do patch é posterior à do disco, aceitam a mídia física como licença local. *Recompile* mostrou o limite do método: quando o disco contém uma revisão mais nova que o patch, o sistema trata as instalações como versões diferentes e não usa o disco apenas como licença.

O experimento com *Elden Ring* parte de uma situação favorável. O disco contém `01.000.000`; o retail patch preservado é `01.018.001`, compatível com o firmware `13.60`. O pacote oficial tem 65.184.595.968 bytes, foi reconstruído a partir de 17 partes e já teve todas elas verificadas contra os hashes do manifesto da Sony.

## Protocolo experimental v0.4.0 — patch-first

Esta é a ordem de trabalho que pretendo validar:

1. Baixar o manifesto e todas as partes do retail update mais recente compatível com o firmware `13.60`, verificar os hashes declarados e reconstruir o PKG original.
2. Com o jogo ausente do console, reproduzir o estado mínimo de um download órfão concluído para que o PatchDL liste o título como update disponível.
3. Instalar somente o retail patch, sem instalar antes a versão-base do disco.
4. Inserir o disco e iniciar o jogo pela instalação patch-only, usando a mídia apenas como licença. Registrar qualquer tentativa de reinstalação, substituição ou consulta online antes de prosseguir.
5. Com a versão mais recente em execução, fazer seu dump de referência com o PS5 App Dumper e preservar logs e metadados.
6. Sem alterar o dump, criar uma working copy com compressão Zstandard no nível *medium*. Essa é uma solução transitória enquanto a criação nativa de fake PKG não estiver disponível no firmware `13.60`.
7. Mover a working copy para fora dos diretórios examinados pelo ShadowMount e somente então desinstalar do console a versão atualizada. Depois, devolvê-la ao alcance do ShadowMount, montá-la e validar sua execução sem o disco; ao final, afastá-la novamente antes da instalação-base.
8. Instalar exclusivamente a versão-base do disco, sem update, executá-la e fazer um segundo dump de referência.
9. Conectar o armazenamento ao PC e produzir os fingerprints de todos os artefatos: dumps, manifestos, PKG oficial e working copy. Comparar também as árvores base e atualizada.
10. Depois das verificações e do teste da working copy, substituir os dumps intermediários e o dump atualizado por tombstones, preservando manifestos, hashes, metadados, logs e as informações necessárias para identificar exatamente o material removido.

## Controles antes de apagar qualquer payload

O passo 10 é uma política de economia de espaço, não parte da aquisição. Nenhum dump será convertido em tombstone antes de cumprir estes controles:

- os manifestos SHA-256 e de tamanhos precisam ter sido gerados e conferidos;
- os hashes dos próprios manifestos precisam estar registrados;
- a working copy precisa ter hash integral e ter sido executada sem o disco;
- o teste deve incluir início, algum tempo de jogo e, quando possível, salvar, encerrar e retomar;
- as diferenças entre a versão-base e a atualizada precisam estar documentadas;
- o PKG oficial e seu conjunto de preservação precisam continuar guardados separadamente;
- o tombstone deve registrar localização anterior, versão, Title ID, quantidade de arquivos, tamanho aparente e motivo da remoção.

A versão-base merece uma decisão separada. Como ela representa diretamente a prensagem física e pode não ser reconstruível byte a byte a partir do disco pelo mesmo processo de dump, o protocolo não presume automaticamente que seu payload será apagado. A princípio, os candidatos a tombstone são os dumps redundantes ou substituídos pela working copy validada; a retenção do dump-base será decidida depois do fingerprint e da comparação.

## Preparação já concluída

Antes da instalação, já estão prontos:

- identificação do disco como `PPSA04610`, versão-base `01.000.000`;
- identificação de `01.018.001` como update-alvo compatível com o firmware;
- manifesto original e retail PKG reconstruído;
- verificação das 17 partes e fingerprint do PKG;
- cópia do PKG e do estado mínimo de download concluído preparada inicialmente no armazenamento USB usado pelo PatchDL.

## Primeira descoberta: o estado órfão não foi importado do USB

Depois de remover *Elden Ring* do console, conectei o HD com a pasta completa em `patchdl/PPSA04610/` e iniciei o PatchDL. O jogo ausente não apareceu na lista. Portanto, apenas manter o PKG e o `state.json` sob a pasta `patchdl` de `usb0` não fez esta versão do programa importar ou apresentar o download órfão.

Copiei então a mesma pasta para `/data/patchdl/PPSA04610/`, na memória interna do console, e reiniciei o PatchDL. Desta vez *Elden Ring* apareceu com o botão **Instalar**. A instalação patch-only de `01.018.001` foi iniciada e ainda estava em andamento no momento deste registro.

Essa observação separa dois comportamentos: o PatchDL pode conservar ou acessar um PKG no USB em outros fluxos, mas seu scanner de downloads órfãos não reconheceu automaticamente este estado a partir dali. Para forçar a listagem de um jogo completamente ausente, `/data/patchdl` continua sendo, por enquanto, o local confirmado.

## Estado patch-only antes do dump

Com a instalação concluída e antes de iniciar o dump, fiz uma inspeção somente leitura por FTP. O estado observado foi:

- `/user/app/PPSA04610`: presente;
- `/user/patch/PPSA04610`: ausente;
- `/user/appmeta/PPSA04610`: presente;
- `app.pkg`: 65.184.595.968 bytes, exatamente o tamanho do PKG preservado;
- Content Version: `01.018.001`;
- Origin Content Version: `01.000.000`;
- Required System Software Version: `0x1360000000000000`;
- Application DRM Type: `standard`.

O `app.json` registra 17 partes, o tamanho original integral e o manifesto local servido pelo PatchDL. Em `/data/patchdl/PPSA04610/`, o PKG, `state.json`, CRC, manifesto local e ícone continuavam presentes. O estado marcava 65.184.595.968 de 65.184.595.968 bytes concluídos, com as 17 partes completas.

A ausência de `/user/patch/PPSA04610` e a presença do PKG integral sob `/user/app` confirmam que o retail update foi registrado como aplicação completa, não como uma árvore de patch separada. O snapshot textual foi preservado em [`pre-dump-patch-only-state.txt`]({{ '/evidence/elden-ring-patch-first-2026-11-20/pre-dump-patch-only-state.txt' | relative_url }}).

Com o disco `01.000.000` inserido, iniciei essa instalação patch-only `01.018.001`. O jogo abriu normalmente e chegou à tela de início. O teste foi deliberadamente curto e não demonstra ainda estabilidade durante uma sessão prolongada, mas confirma o ponto central desta etapa: uma revisão-base muito anterior no disco pôde servir como licença local para a aplicação completa instalada a partir do retail update mais novo.

## Dump atualizado concluído

O dump patch-only foi concluído com o PS5 App Dumper v2.10. A execução final começou às 00:28:18 e terminou às 01:57:17 de 21 de novembro, totalizando 5.339 segundos. O `dump-info.json` registra:

- estado `done`;
- 156.112.555.864 bytes processados, aproximadamente 145,391 GiB;
- descriptografia ligada;
- conversão para FSELF desligada;
- backport desligado;
- modo de split PS4 `3`, sem efeito para este título de PS5.

O log final tem 789 linhas e 93.704 bytes. Ele chega a 100%, informa média final de 27,93 MB/s e não contém mensagens correspondentes a erro ou falha. A extração direta dos 22 metadados do pacote também terminou com `SUCCESS`. A pasta resultante é `PPSA04610-app0_ELDEN_RING`, acompanhada de `dump-info.json` e log.

Uma segunda inspeção por FTP confirmou que, depois do dump, `/user/app/PPSA04610` e `/user/appmeta/PPSA04610` continuavam presentes e `/user/patch/PPSA04610` continuava ausente. Portanto, o dumper não alterou a forma de registro observada antes da extração. O snapshot pós-dump está em [`post-dump-state.txt`]({{ '/evidence/elden-ring-patch-first-2026-11-20/post-dump-state.txt' | relative_url }}).

## Duas falhas do Dump Forge antes do pack

Tentei criar no próprio PS5 a working copy comprimida em Zstandard, nível médio. Nas duas tentativas, o Dump Forge conseguiu ler e interpretar o diretório do dump, mas fechou antes de apresentar o nome de saída derivado do Product ID e da versão. A etapa de pack não chegou a começar.

Uma inspeção posterior não encontrou arquivo de *Elden Ring*, imagem parcial ou novo diretório de saída em `pkg-build-output` ou na área de working images do acervo. Os registros disponíveis em `/data/dumpforge` cobrem apenas a inicialização normal do servidor da ferramenta; não há backtrace, relatório de crash ou log da operação. Naquele ponto do experimento, portanto, ainda não existia working copy e o dump atualizado não podia ser convertido em tombstone.

O incidente está preservado em [`dump-forge-console-crash.txt`]({{ '/evidence/elden-ring-patch-first-2026-11-20/dump-forge-console-crash.txt' | relative_url }}).

## Working copy produzida no Linux

No PC, instalei a versão oficial Linux x86-64 do PS5 Dump Forge v0.5.6 e repeti a operação pelo CLI. A inspeção reconheceu corretamente `PPSA04610`, versão `01.018.001`, firmware `13.60`, 114.760 arquivos de origem e nenhum backport existente. O pack foi configurado como pasta Zstandard no nível `9`, equivalente ao preset médio, com chunks de 256 KiB.

A operação terminou com sucesso:

- 114.732 arquivos incorporados aos packs;
- 30 arquivos de sistema e runtime mantidos soltos;
- 18 volumes Zstandard;
- 114.762 arquivos lógicos na working copy;
- 156.149.281.464 bytes lógicos;
- 75.131.427.965 bytes físicos na saída.

O Dump Forge instalou o runtime Zstandard em `fakelib/libSceAmpr.sprx`, gerou um novo `ampr_emu.index` e publicou atomicamente o diretório final `Elden Ring - PPSA04610 - 01.018.001`. O dump de origem permaneceu intacto.

Esta execução usou a verificação rápida padrão, não `--full-verify`. Ainda assim, ela conferiu 116.093.678.264 dos 156.149.281.464 bytes lógicos em 116.321 amostras BLAKE3, além de validar o índice, os 18 cabeçalhos dos volumes, o conjunto de caminhos, os tamanhos e os diretórios vazios. Todos os controles passaram. O registro completo está em [`dump-forge-linux-pack.txt`]({{ '/evidence/elden-ring-patch-first-2026-11-20/dump-forge-linux-pack.txt' | relative_url }}).

## Fingerprints do dump e da pasta intermediária

Gerei os dois manifestos do dump patch-only excluindo `sce_sys/`, de acordo com o protocolo de referência:

- 114.735 arquivos regulares;
- 156.057.680.842 bytes aparentes;
- SHA-256 do manifesto de conteúdo: `a6ee0cb7ca0a2bad956735d176104c567a87a8e57cd71c6b7427a5016b3e46c0`;
- SHA-256 do manifesto de tamanhos: `02c5c2e3545467bba0354bd4f6c0e9aca952abe902ac789471cf7b1e1b1f9a4d`.

Para a pasta Zstandard intermediária, o fingerprint cobre todos os arquivos físicos, inclusive `sce_sys/`, o runtime e os volumes comprimidos:

- 49 arquivos regulares;
- 75.145.310.275 bytes aparentes;
- SHA-256 do manifesto de conteúdo: `5cea4b45252ba071199b5ee4d056b82f9c8d17f3d0fa112e3ea8323533e3b9c2`;
- SHA-256 do manifesto de tamanhos: `9ec019f88a25d648061363015a4cb2882f5d0e2230d3f6fea6e5547cc96a7b59`.

Em ambos os casos, os manifestos SHA-256 e TSV possuem exatamente a mesma quantidade de entradas. Recalculei também os hashes dos quatro manifestos e obtive os mesmos valores emitidos durante sua geração. O resumo está em [`fingerprints.txt`]({{ '/evidence/elden-ring-patch-first-2026-11-20/fingerprints.txt' | relative_url }}).

Esse segundo fingerprint não representa a imagem de trabalho definitiva: a conversão no Linux havia usado por engano o destino `folder`, em vez de `ffpkg`. Mantive o registro como evidência da entrada intermediária, mas ele não substitui o SHA-256 do FFPKG.

## FFPKG e validação no console

Converti posteriormente a pasta Zstandard já pronta em um FFPKG, sem repetir a compressão dos arquivos lógicos. A imagem foi colocada ao alcance do ShadowMount+ e executada com sucesso no console, sem problema visível. Portanto, a working copy de `01.018.001` está funcional.

O FFPKG definitivo possui 75.301.584.896 bytes e SHA-256 `9f0d5296153750a5eded831310d6511baa00362d262874eda8d32af1702e96a7`. Seu manifest de uma linha foi guardado ao lado da imagem. Com a execução no console e o fingerprint final concluídos, a working copy está validada.

A versão-base `01.000.000` já possui dump antigo e fingerprint incorporados ao acervo; embora essa extração não tenha `dump-info.json` nem log específico, não é necessário repeti-la para fechar o ciclo atual.

Depois de uma revisão separada, substituí o payload do dump patch-only por um tombstone. Permaneceram os dois manifestos completos, `dump-info.json`, `param.json`, o retail PKG verificado, o dump-base, as evidências do experimento e o FFPKG funcional. O registro da remoção está em [`README.md`]({{ '/evidence/elden-ring-01.018.001-tombstone/README.md' | relative_url }}). Essa decisão recuperou 156.057.680.842 bytes aparentes sem remover a base nem a working copy.

#ps5 #elden-ring #patchdl #patch-only #protocolo #preservacao
