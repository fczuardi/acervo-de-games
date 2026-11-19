---
title: "Recompile — preparando um teste patch-only com um disco ainda não usado"
date: 2026-11-19 17:55:00 -0300
---

Comprei recentemente uma cópia física de *Recompile* para PS5, `PPSA03183`. O disco ainda não foi inserido neste console e nunca serviu para iniciar o jogo. Isso cria uma oportunidade rara: testar uma instalação feita somente a partir do retail patch oficial antes que exista qualquer instalação ou validação anterior associada a essa mídia.

O objetivo não é evitar o disco. Pelo contrário, quero observar separadamente duas funções que normalmente aparecem juntas: o patch fornece o conteúdo instalado, enquanto o disco deve fornecer a licença local necessária para executá-lo.

## Por que este jogo é um bom candidato

O ProsperoPatches identifica `01.004.000` como a atualização mais recente e informa firmware mínimo `03.21.00.00`, bem abaixo do `13.60` do console. O pacote tem cerca de 1,5 GB, tamanho pequeno para um jogo de PS5, mas plausível neste caso: a edição de PC também é compacta. Portanto, o tamanho sozinho não demonstra que o update dependa dos arquivos da versão-base.

O experimento anterior com *Demon's Souls* mostrou que um retail update pode ocupar sozinho `/user/app/`, iniciar depois que o disco fornece a licença e produzir um dump igual ao da instalação convencional fora de `sce_sys/`. Isso não permite generalizar o resultado. *Recompile* servirá como um segundo caso, com outra publicadora, outro jogo e, principalmente, um disco que ainda não foi usado no console.

## O patch preservado

Baixei o manifesto original e montei o retail PKG com o [`fetchpkg`](https://github.com/ps5-payload-dev/fetchpkg), no commit `10c9bb95f651d594ba254c104ac96d0bc836ed2d`. O manifesto descreve duas partes contíguas, sem lacunas ou sobreposições:

- tamanho final: 1.604.976.640 bytes;
- primeira parte: 1.553.006.592 bytes;
- segunda parte: 51.970.048 bytes;
- manifesto: 1.067 bytes, SHA-256 `752bbb8efbd0738c305dd2441738f2ef04833ae5a87bde65231e5e38650734e8`;
- PKG montado: SHA-256 `b7f4e3994d9a193017a3bd4d70728c153d795bbf91e562fdf6f1a71510679127`.

As duas partes foram verificadas individualmente pelos SHA-256 declarados pela Sony. A soma de seus tamanhos coincide com o tamanho final, e o conjunto de preservação contém o manifesto original, registro de aquisição, relatório por partes, verificação integral e checksums agregados. As URLs de distribuição permanecem no acervo privado e não são publicadas.

## Sequência planejada

Primeiro vou instalar o patch com o PatchDL sem inserir o disco. Depois registrarei por FTP onde e com que tamanho a aplicação foi instalada. A primeira tentativa de execução também será feita sem o disco, para verificar se o console pede validação online, mídia física ou apresenta outro comportamento.

Só então inserirei o disco pela primeira vez. Se o jogo abrir sem copiar a base, repetirei a inspeção do filesystem e farei um teste curto de execução. Por fim, pretendo extrair a instalação com o PS5 App Dumper e criar uma working copy, preservando tanto o dump descriptografado quanto o retail PKG que permitiu reproduzi-lo.

Ainda não há resultado de instalação ou de licença. Também não está demonstrado que o patch contenha o jogo completo, que o disco será aceito sem uma cópia da base ou que a working copy iniciará offline. Este post registra a hipótese, os controles e o estado inicial antes de o disco tocar o console; os resultados serão documentados separadamente.

#ps5 #recompile #patchdl #patch-only #midia-fisica #preservacao
