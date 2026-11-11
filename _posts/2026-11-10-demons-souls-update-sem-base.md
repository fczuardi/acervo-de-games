---
title: "Demon's Souls 01.007.000 instalado sem a base do disco"
date: 2026-11-10 15:30:00 -0300
---

Hoje fiz um experimento para entender se uma instalação de disco pode ser substituída por um update oficial de PS5 usado sozinho.

Usei novamente Demon's Souls, `PPSA01342`, no firmware 13.60. O retail PKG `01.007.000` já estava preservado e verificado. A pergunta era simples: esse pacote depende dos arquivos da versão `01.000.000` instalada pelo disco ou consegue ocupar sozinho o lugar da aplicação?

## Preparação

Antes de mexer na instalação, revisei o código do PatchDL v0.3.12. Para jogos de PS5, o projeto possui um fluxo de substituição que remove a aplicação inteira, espera ela desaparecer e depois instala o pacote baixado. O próprio README diz que o disco continua sendo usado como licença.

Também registrei por FTP o estado da instalação limpa do disco. Ela aparecia em `/user/app/PPSA01342/`, com um `app.pkg` de 52.083.556.352 bytes. Não existia uma pasta correspondente em `/user/patch/`.

Mas esse não foi o fluxo que a interface ofereceu para Demon's Souls naquele estado. Depois do download, o único botão disponível era **Instalar**. Antes de usá-lo, conferi os metadados internos apresentados pelo PatchDL: a base instalada e a base esperada pelo pacote eram ambas `01.000.000`, e `base_fits` estava como verdadeiro. Portanto, aquele botão seguiria a instalação normal do update sobre uma base considerada compatível; ele não chamaria a rotina de substituição com exclusão que eu queria observar.

Por isso removi deliberadamente a instalação-base pela própria interface nativa do PS5. Não foi uma tentativa de imitar às cegas o PatchDL: foi uma forma de separar as duas operações e estabelecer, por inspeção, a condição inicial do experimento. Depois do **Delete**, conferi por FTP que `/user/app/PPSA01342/`, `/user/patch/PPSA01342/` e `/user/appmeta/PPSA01342/` tinham desaparecido. O PKG já baixado pelo PatchDL continuava guardado em `/data/patchdl/`.

O disco ficou ejetado durante toda a instalação seguinte.

## Instalação somente do update

Com a base ausente e depois de reiniciar o programa para ele reler o estado do console, o PatchDL passou a mostrar Demon's Souls como não instalado e ofereceu **Instalar 01.007.000**. Foi esse botão, agora sem uma base presente, que usei.

A primeira tentativa falhou com `NW-102261-2`. O instalador nativo dizia que não conseguia se conectar ao servidor. A inspeção mostrou que o PatchDL serve localmente as partes do PKG por `127.0.0.1:12880` e que esse servidor havia parado de responder. Depois de abrir novamente o PatchDL e escolher **Try Again**, a cópia prosseguiu normalmente.

O processo terminou com a notificação de que Demon's Souls estava pronto para jogar. A tela de informações indicava o download como concluído, mas ainda mostrava a inicialização como inelegível.

Uma nova inspeção por FTP encontrou:

- `/user/app/PPSA01342/app.pkg`: 53.805.318.144 bytes;
- versão registrada: `01.007.000`;
- `/user/appmeta/PPSA01342/`: presente;
- `/user/patch/PPSA01342/`: ausente.

O tamanho do `app.pkg` instalado é exatamente o tamanho do retail update preservado. Portanto, neste caso o update não foi registrado como uma camada separada sobre a base. Ele ocupou sozinho o lugar da aplicação completa em `/user/app/`.

## O papel do disco

Primeiro tentei abrir o jogo ainda com o disco ejetado. O PS5 recusou com esta mensagem:

> Can't use this content. Can't connect to the server to verify your license. Wait a while, and then try again.

Curiosamente, a mensagem não pediu o disco. Sem ele, essa instalação entrou no caminho de verificação online de licença.

Depois inseri o disco físico correspondente. O botão mudou imediatamente para **Play Game**, sem começar uma cópia da versão-base e sem novo download.

O jogo abriu, chegou à tela inicial, encontrou meu save e ofereceu **Continue**. Carreguei Gates of Boletaria e joguei normalmente por um trecho curto. Não observei problema de áudio, texturas ou desempenho nesse teste.

Depois de fechar o jogo, repeti a inspeção. O `app.pkg` continuava com 53.805.318.144 bytes, `/user/patch/PPSA01342/` continuava ausente e os pequenos arquivos `app.json`, `app.xml` e `param.json` estavam idênticos aos lidos antes da execução. Inserir o disco e jogar não restaurou a base `01.000.000`.

## Dump da instalação patch-only

Depois desse teste, usei o PS5 App Dumper v2.10 para extrair também a instalação patch-only. Mantive a mesma configuração dos dumps anteriores: modo FLAT, descriptografia ligada, conversão para FSELF desligada e sem backport.

O processo levou 2h03m30s. O dumper registrou 88.025.089.248 bytes e terminou com estado `done`. A árvore resultante contém 223.265 arquivos regulares, somando 88.040.148.641 bytes aparentes.

Gerei os manifestos SHA-256 e de tamanhos seguindo o [protocolo de preservação v0.3.0](https://fczuardi.github.io/acervo-de-games/2026/11/08/dump-de-referencia-base-v1.html), novamente excluindo `sce_sys/`. Os dois conjuntos, com 223.238 caminhos, ficaram byte a byte idênticos aos manifestos do dump `01.007.000` obtido anteriormente a partir da instalação convencional base+update:

- manifesto SHA-256: `f78516ad791e595fddc6ca6cab25c9a75dbf496a360cf1f5fa38a209431a88fb`;
- manifesto de tamanhos: `b6a6d48b3adde38ee81dbecd465f83dcb38784c932976d3f21a7175aaf81b58e`;
- `eboot.bin` descriptografado: `4a6ca8a2904d02a9ff11aebcb10379c89974cd9bff1a37e09c21a7e782447674`.

Também comparei separadamente `sce_sys/`. Os 27 arquivos presentes nos dois dumps têm SHA-256 idêntico. A única diferença observada nas árvores completas foi `sce_sys/disc_info.dat`, com 6.640 bytes, presente no dump convencional e ausente no patch-only. Isso explica exatamente a diferença de um arquivo e 6.640 bytes entre as duas extrações.

O arquivo é quase todo preenchido com zeros. No começo aparecem o Title ID, alguns inteiros e um bloco binário de 32 bytes que muda entre a base e o update. Encontrei a mesma estrutura, com outro Title ID e outro bloco binário, em um dump de Death Stranding Director's Cut vindo de disco e posteriormente comprimido com LZ4. Isso confirma que o formato não é particular de Demon's Souls, mas ainda não identifica com segurança o significado desses campos.

O nome sugere que `disc_info.dat` registra informação ligada à instalação física, o que combina com o experimento. O resultado seguro é mais simples: no nível dos arquivos descriptografados pelo App Dumper, o conteúdo do jogo é igual; a única diferença encontrada está nesse metadado de `sce_sys`.

## O que ficou demonstrado

Para esta versão de Demon's Souls:

1. o retail update oficial `01.007.000` pôde ser instalado sem a base do disco presente;
2. o resultado foi registrado como uma aplicação completa em `/user/app/`;
3. sem o disco, o console tentou verificar uma licença online e não abriu o jogo;
4. o disco físico foi aceito imediatamente como licença local;
5. o jogo iniciou, carregou um save e permitiu gameplay sem reinstalar a base;
6. o dump descriptografado resultante é idêntico ao dump convencional fora de `sce_sys/`, e a única diferença na árvore completa é a ausência de `disc_info.dat`.

Isso não prova jogabilidade completa, nem permite generalizar o comportamento para todo update de PS5. A igualdade dos dumps também não significa que os registros internos das duas instalações sejam iguais. É o resultado observado neste pacote, neste jogo e neste firmware.

Também não testei, nesta execução, a rotina automática de substituição do PatchDL de ponta a ponta. Revisei seu funcionamento no código, mas a remoção efetiva da base foi feita pela interface nativa do PS5 porque o botão inicialmente oferecido pelo PatchDL faria uma atualização normal sobre a base compatível.

Guardei no repositório as pequenas evidências textuais do experimento: revisão do fluxo do PatchDL, estados do filesystem, hashes dos metadados e o registro da falha intermediária. O PKG, arquivos do jogo, licenças e URLs de distribuição não são publicados.

#ps5 #demons-souls #patchdl #midia-fisica #preservacao
