---
title: "My First Gran Turismo — um dump digital que não quero perder"
date: 2026-11-18 17:00:00 -0300
---

Ao revisar dumps que fiz antes de começar este acervo, encontrei uma cópia de *My First Gran Turismo*, `PPSA24156`, na versão `01.010.000`. O jogo é gratuito na PSN, mas isso não torna sua preservação simples: ele é distribuído apenas em formato digital e não tenho um disco que possa servir como licença local no futuro.

Esse detalhe ficou mais importante depois do experimento com *Demon's Souls*. Naquele caso, consegui instalar sozinho o retail update oficial `01.007.000`. Sem o disco, o PS5 tentou verificar a licença pela rede e recusou a inicialização. Ao inserir a mídia física, o mesmo conteúdo abriu imediatamente, sem reinstalar a base. O disco forneceu uma rota offline para demonstrar a licença.

Para *My First Gran Turismo*, essa rota não existe. Se eu remover a instalação, perder o acesso à conta, ou o serviço deixar de oferecer o título, não posso recorrer a uma mídia física para repetir o teste. Gratuito não significa independente da infraestrutura de distribuição e licenciamento.

## Working copy

Produzi uma working copy FFPKG de `01.010.000`, com 14.807.597.056 bytes. O SHA-256 da imagem final é `c2cd23c9f4e67b87948d6be2dde3760574a66f377fb64b5a31eadf21e1e2a8e1`; o manifest de uma linha está guardado ao lado do arquivo. A imagem foi montada e executada com sucesso no console, encerrando a validação funcional da working copy.

## O dump encontrado

O `dump-info.json`, preservado no diretório pai da extração, registra uma
execução concluída do PS5 App Dumper v2.10 em 19 de outubro de 2026. O processo
começou às 13:10:37, terminou às 13:25:55 e levou 15m18s. Os timestamps de 20
de outubro encontrados na árvore provavelmente correspondem a uma cópia ou
movimentação posterior dos arquivos.

Os dados observáveis são:

- Product ID: `PPSA24156`;
- Content ID: `UP9000-PPSA24156_00-MYFRSTGT00000000`;
- versão observada em `sce_sys/param.json`: `01.010.000`;
- master version declarada: `01.00`;
- firmware mínimo codificado: `0x1020000000000000`;
- estado registrado pelo dumper: `done`;
- bytes reportados pelo dumper: 25.939.578.814;
- opções: descriptografia e conversão FSELF ligadas, backport desligado e
  `split=3`;
- 6.182 arquivos regulares;
- 26.060.309.023 bytes aparentes.

O `eboot.bin` tem 109.163.961 bytes e SHA-256 `7e03d8f703f1cd7dc2cc9e6c55318450a6701725a6f66a183a6489e519bb7118`. O `param.json` tem SHA-256 `2a64fb8f216ce326ff36f34b5b92807ecc69ce0d73bc5f3aa60ef68fdc14cbc8`.

O `dump-info.json` tem SHA-256
`aea1b80d9f9b0fb1dcc102478ef07b5f95e75b19a8953ec97ccda787185fa1da`.
Ainda assim, este dump é anterior ao protocolo atual do acervo: não encontrei
um log detalhado da extração.
Também conferi o `log.txt` compartilhado do App Dumper, mas seu primeiro
registro é de 20 de outubro e não há nele uma entrada para `PPSA24156`.
Portanto, a data e a duração acima vêm do `dump-info.json`, não desse log.
Depois de incorporar a árvore ao acervo, gerei os manifestos pelo protocolo
atual, excluindo `sce_sys/`: são 6.161 arquivos e 26.025.774.673 bytes
aparentes. O manifesto SHA-256 tem hash
`5f5cb31f8e3ec73f4b7d5da3224da58177aabb28f13b9fadafd00e6fca11885c`;
o manifesto de tamanhos tem hash
`9341c132d8ae6c2d09f17aff44bee26b3c43dc51d349c079048694fa463ae777`.

O ProsperoPatches identifica `01.010.000` como a versão mais recente e informa
firmware mínimo `10.20.00.06`, abaixo do `13.60` do console. Neste caso, o dump
antigo já corresponde à versão mais recente compatível.

## Retail PKG oficial

Preservei posteriormente o manifesto original e o retail PKG de
`01.010.000`. O pacote tem 13.099.401.216 bytes e SHA-256
`7a8db7f03603a55529410b158d0733c0f9492352164332e8a9b933bfaca94a11`.
O manifesto tem SHA-256
`b74bdf2fff0f9ba773295e515835e2037344ce1153478985fd9e5bf584493036`.

As cinco partes contíguas conferiram com os SHA-256 declarados pela Sony. O
manifesto revela uma composição regional peculiar: quatro partes pertencem a
`PPSA24155`, e um suplemento final de 40.960.000 bytes pertence a
`PPSA24156`. Não se trata de uma combinação inferida localmente; é a montagem
determinada pelo próprio manifesto oficial de `PPSA24156`.

O único PKG retido foi organizado diretamente no formato esperado pelo
PatchDL, sob
`PPSA24156/UP9000-PPSA24156_00-MYFRSTGT00000000.pkg`, acompanhado de um
`state.json` concluído. Os registros de aquisição e verificação e o manifesto
agregado foram atualizados para esse caminho sem reler nem duplicar o arquivo.

## Por que vou mantê-lo

Nos jogos físicos do lote, um dump intermediário pode se tornar redundante quando preservo a base do disco, o retail patch oficial e evidência suficiente para reproduzir a instalação. Aqui o risco é diferente. O dump existente pode ser a única cópia local que tenho do conteúdo descriptografado em um estado que já passou pelo licenciamento digital do console.

Isso não quer dizer que o dump contenha ou substitua uma licença válida, nem garante que uma imagem derivada vá iniciar offline. São perguntas que ainda precisam de testes separados. Significa apenas que apagar o conteúdo antes desses testes eliminaria uma evidência que não tenho como recriar com um disco.

Com dump, fingerprints, retail PKG, working copy e teste funcional concluídos,
o ciclo aplicável a este título digital está fechado. Isso não quer dizer que
o dump contenha ou substitua uma licença válida em outro console. Por não
existir disco e por a aquisição depender da PSN, o dump descriptografado não
será transformado em tombstone.

#ps5 #myfirstgranturismo #gran-turismo #digital-only #preservacao
