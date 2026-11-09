---
title: "Teste do dump de Demon's Souls 01.007.000 sem o disco"
date: 2026-11-09 21:30:00 -0300
---

Depois de preservar o dump descriptografado de Demon's Souls `01.007.000`, fui testar se conseguia usá-lo para abrir o jogo sem o disco original.

Mantive o dump de referência intacto e fiz todo o trabalho em uma cópia separada. Antes de começar, conferi essa cópia contra o manifesto SHA-256 já preservado. Depois disso ela passou a ser apenas uma cópia de trabalho modificável.

## Ajustes na cópia

O dump havia sido feito com a opção FSELF desligada de propósito. Isso preservou os executáveis descriptografados, mas eles ainda não estavam prontos para carregar nesse ambiente de homebrew.

Usei a função FSELF do PS5 App Dumper v2.10 na cópia de trabalho. Quatro arquivos foram convertidos:

- `eboot.bin`;
- `sce_module/libc.prx`;
- `sce_module/libSceNpCppWebApi.prx`;
- `sce_sys/about/right.sprx`.

Sem essa conversão, o jogo encerrava imediatamente com o erro `CE-100008-9`. Com os FSELF, ele passou a iniciar, mas ficava parado numa tela preta.

Demon's Souls também depende do APR/AMPR do sistema. Usei o Alembic para gerar o `ampr_emu.index` e adicionar o `libSceAmpr.sprx` à `fakelib`. A permissão do módulo precisou ser corrigida para `0777`; sem isso, o carregador recusava o arquivo por seus atributos de montagem.

Também experimentei um substituto de PlayGo vindo de outro jogo. O resultado foi um `SIGBUS` reproduzível poucos segundos depois da abertura. Esse arquivo não fazia parte da solução e foi removido.

## Teste em pasta

Mesmo com FSELF e AMPR corretos, a pasta copiada para o M.2 continuava numa tela preta. Depois de procurar relatos de outras pessoas, encontrei o mesmo comportamento descrito para Demon’s Souls no firmware 13.60: pasta no armazenamento interno sem avançar, mas imagem exFAT funcionando.

Parecia ser uma diferença de filesystem e montagem, não corrupção do dump. No modo pasta, o ShadowMount+ apresentava diretamente a árvore do M.2 via `nullfs`.

## Imagem exFAT

Numa imagem exFAT, o ShadowMount+ monta primeiro o filesystem por LVD e só então expõe o jogo ao sistema.

Usei o PS5 Dump Forge para criar uma imagem exFAT sem compressão e com clusters de 64 KiB. A imagem resultante tem 100.687.872.000 bytes.

A primeira tentativa de conversão falhou porque eu havia deixado o jogo aberto e o `playgo.log` mudou enquanto a fonte era lida. Fechei o jogo, repeti o trabalho com a árvore estável e a verificação terminou sem erro.

O ShadowMount+ montou a imagem, instalou o atalho e iniciou o jogo. Joguei o começo por aproximadamente 19 minutos. Não observei problemas de texturas, áudio ou desempenho, e o processo terminou normalmente quando fechei o jogo.

## FFPKG com Zstandard

Com a imagem exFAT servindo como controle funcional, fiz uma segunda conversão no Dump Forge. Desta vez empacotei os arquivos com Zstandard no nível médio e usei uma imagem FFPKG.

Essa versão, com 57.819.987.968 bytes, também abriu normalmente. Joguei por mais tempo, confirmei o salvamento e, depois de fechar e abrir novamente, consegui retomar o progresso. Até aqui, a working image FFPKG com Zstandard apresentou desempenho normal e ocupa menos espaço que a imagem exFAT sem compressão.

Isso não equivale a testar o jogo inteiro. Não validei todas as áreas, modos, idiomas ou situações de salvamento. O teste de hoje foi:

1. partir do dump preservado e verificado;
2. produzir uma cópia de trabalho modificada sem alterar a referência;
3. iniciar o jogo sem o disco;
4. jogar o trecho inicial com desempenho aparentemente normal;
5. salvar, fechar, abrir novamente e retomar o progresso.

Pretendo manter apenas uma imagem de trabalho funcional. As imagens intermediárias podem ser recriadas a partir do dump de referência e destas anotações.

Nenhum arquivo do jogo é disponibilizado neste site. Este é somente um registro do procedimento, dos testes e do resultado.

#ps5 #demons-souls #preservacao #shadowmount #dump-forge
