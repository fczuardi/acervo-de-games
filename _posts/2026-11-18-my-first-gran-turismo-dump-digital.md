---
title: "My First Gran Turismo — um dump digital que não quero perder"
date: 2026-11-18 17:00:00 -0300
---

Ao revisar dumps que fiz antes de começar este acervo, encontrei uma cópia de *My First Gran Turismo*, `PPSA24156`, na versão `01.010.000`. O jogo é gratuito na PSN, mas isso não torna sua preservação simples: ele é distribuído apenas em formato digital e não tenho um disco que possa servir como licença local no futuro.

Esse detalhe ficou mais importante depois do experimento com *Demon's Souls*. Naquele caso, consegui instalar sozinho o retail update oficial `01.007.000`. Sem o disco, o PS5 tentou verificar a licença pela rede e recusou a inicialização. Ao inserir a mídia física, o mesmo conteúdo abriu imediatamente, sem reinstalar a base. O disco forneceu uma rota offline para demonstrar a licença.

Para *My First Gran Turismo*, essa rota não existe. Se eu remover a instalação, perder o acesso à conta, ou o serviço deixar de oferecer o título, não posso recorrer a uma mídia física para repetir o teste. Gratuito não significa independente da infraestrutura de distribuição e licenciamento.

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
um log detalhado da extração nem manifestos completos de hashes e tamanhos.
Também conferi o `log.txt` compartilhado do App Dumper, mas seu primeiro
registro é de 20 de outubro e não há nele uma entrada para `PPSA24156`.
Portanto, a data e a duração acima vêm do `dump-info.json`, não desse log.
Essas evidências ainda precisam ser produzidas antes de tratar o conjunto como
equivalente aos dumps feitos pelo fluxo atual.

Também não afirmo ainda que `01.010.000` era a versão-base ou a versão mais recente compatível no momento da extração. É apenas a versão que o próprio dump registra. Antes do jailbreak eu usava o que já estava instalado no console, então este conteúdo pode ter vindo de uma atualização intermediária.

## Por que vou mantê-lo

Nos jogos físicos do lote, um dump intermediário pode se tornar redundante quando preservo a base do disco, o retail patch oficial e evidência suficiente para reproduzir a instalação. Aqui o risco é diferente. O dump existente pode ser a única cópia local que tenho do conteúdo descriptografado em um estado que já passou pelo licenciamento digital do console.

Isso não quer dizer que o dump contenha ou substitua uma licença válida, nem garante que uma imagem derivada vá iniciar offline. São perguntas que ainda precisam de testes separados. Significa apenas que apagar o conteúdo antes desses testes eliminaria uma evidência que não tenho como recriar com um disco.

Os próximos passos são gerar manifestos SHA-256 e de tamanhos pelo protocolo atual, registrar os metadados que podem ser publicados sem expor dados sensíveis e criar uma working copy separada. Depois quero testar, com a rede desligada, até onde essa cópia consegue iniciar no console e documentar o resultado sem confundir preservação dos arquivos com preservação do direito de execução.

Por enquanto, a decisão é simples: este dump não será transformado em tombstone. Em um título digital-only, gratuito e dependente da PSN para aquisição, a cópia antiga merece mais cautela, não menos.

#ps5 #myfirstgranturismo #gran-turismo #digital-only #preservacao
