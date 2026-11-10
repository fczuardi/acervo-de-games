---
title: "Demon's Souls 01.007.000 instalado sem a base do disco"
date: 2026-11-10 17:00:00 -0300
---

Hoje fiz um experimento para entender melhor o que acontece quando o PatchDL substitui uma instalação de disco por um update oficial de PS5.

Usei novamente Demon's Souls, `PPSA01342`, no firmware 13.60. O retail PKG `01.007.000` já estava preservado e verificado. A pergunta era simples: esse pacote depende dos arquivos da versão `01.000.000` instalada pelo disco ou consegue ocupar sozinho o lugar da aplicação?

## Preparação

Antes de mexer na instalação, revisei o código do PatchDL v0.3.12. Para jogos de PS5, o fluxo de substituição previsto pelo projeto remove a aplicação inteira, espera ela desaparecer e depois instala o pacote baixado. O próprio README do projeto diz que o disco continua sendo usado como licença.

Também registrei por FTP o estado da instalação limpa do disco. Ela aparecia em `/user/app/PPSA01342/`, com um `app.pkg` de 52.083.556.352 bytes. Não existia uma pasta correspondente em `/user/patch/`.

Baixei o update pelo PatchDL e, para deixar o teste bem separado, removi a instalação-base pela própria interface do PS5. Conferi então que `/user/app/PPSA01342/`, `/user/patch/PPSA01342/` e `/user/appmeta/PPSA01342/` tinham desaparecido. O PKG baixado pelo PatchDL continuava guardado em `/data/patchdl/`.

O disco ficou ejetado durante toda a instalação seguinte.

## Instalação somente do update

Com a base ausente, o PatchDL ofereceu instalar diretamente a versão `01.007.000`.

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

## O que ficou demonstrado

Para esta versão de Demon's Souls:

1. o retail update oficial `01.007.000` pôde ser instalado sem a base do disco presente;
2. o resultado foi registrado como uma aplicação completa em `/user/app/`;
3. sem o disco, o console tentou verificar uma licença online e não abriu o jogo;
4. o disco físico foi aceito imediatamente como licença local;
5. o jogo iniciou, carregou um save e permitiu gameplay sem reinstalar a base.

Isso não prova jogabilidade completa, nem permite generalizar o comportamento para todo update de PS5. É o resultado observado neste pacote, neste jogo e neste firmware.

Guardei no repositório as pequenas evidências textuais do experimento: revisão do fluxo do PatchDL, estados do filesystem, hashes dos metadados e o registro da falha intermediária. O PKG, arquivos do jogo, licenças e URLs de distribuição não são publicados.

#ps5 #demons-souls #patchdl #midia-fisica #preservacao
