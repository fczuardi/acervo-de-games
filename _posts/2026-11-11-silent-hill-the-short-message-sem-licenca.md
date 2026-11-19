---
title: "SILENT HILL: The Short Message e a licença que faltou"
date: 2026-11-11 10:30:00 -0300
---

Hoje tentei preservar e executar `SILENT HILL: The Short Message`, `PPSA04877`, num PS5 com firmware 13.60 mantido fora da PSN.

O jogo foi distribuído gratuitamente na PlayStation Store. Como a única versão disponível nos servidores da Sony parece conter a aplicação completa, quis descobrir se o retail patch poderia ser instalado e usado sozinho por uma conta local sem histórico de PSN.

Primeiro preservei o pacote `01.000.001`. Ele tem 12.148.146.176 bytes, divididos em quatro partes no manifesto da Sony. As quatro foram verificadas durante o download e novamente durante o cálculo do SHA-256 do arquivo montado:

```text
2330b9dab40a0a2cbfba03931459116bca946a616f6e588cc643c5bc70fcfd3c
```

## Instalação direta

Instalei o PKG pelo PS5 Web File Manager, sem jogo-base e sem PatchDL. O instalador aceitou o pacote e terminou normalmente, mostrando o jogo como pronto para jogar.

Por FTP, encontrei um `app.pkg` com os mesmos 12.148.146.176 bytes em `/user/app/PPSA04877/`. Não existia uma pasta em `/user/patch/PPSA04877/`. Portanto, o update havia ocupado sozinho o lugar da aplicação completa.

O `app.json` dessa instalação continha `"fake":true` e descrevia uma única peça apontando para o PKG no USB. Ao abrir o jogo, porém, o PS5 recusou antes da inicialização:

> Can't use this content. Can't connect to the server to verify your license. Wait a while, and then try again.

Na tela de informações, o usuário aparecia como elegível, mas isso não significava que ele possuía a licença do conteúdo.

## Uma segunda instalação pelo PatchDL

Ainda restava a dúvida de que o bloqueio pudesse estar relacionado ao modo como o Web File Manager registrou o pacote.

O PatchDL v0.3.12 reconhecia o jogo instalado como **Sideloaded**, mas não oferecia baixar novamente a única versão existente. Depois da exclusão nativa, o título desaparecia inteiramente da lista. Isso combina com a proposta da ferramenta: ela atualiza jogos já conhecidos pelo console, não mantém um catálogo geral de jogos gratuitos ausentes.

Para testar somente sua rotina de instalação, copiei o PKG preservado para a área de downloads do PatchDL e reproduzi o pequeno `state.json` que ele grava para um download concluído. O código do programa já possui uma rotina para recuperar downloads de PS5 cujo jogo não está mais instalado. Ao reiniciar, o card de Silent Hill apareceu como **Não instalado** e ofereceu **Instalar 01.000.001**.

Desta vez o PatchDL buscou o CRC, gerou um manifesto HTTP local com as quatro partes e entregou o pacote ao instalador nativo. A instalação também terminou normalmente e ficou pronta para jogar.

O resultado no filesystem era diferente:

- o novo `app.json` não continha `"fake":true`;
- as quatro partes apontavam para o servidor local do PatchDL em `127.0.0.1`;
- havia um `app.crc` de 741.464 bytes;
- o `app.pkg` continuava com 12.148.146.176 bytes;
- `/user/patch/PPSA04877/` continuava ausente.

Mesmo assim, ao abrir o jogo recebi exatamente a mesma mensagem de licença.

## O que aprendi

O retail patch de Silent Hill contém uma aplicação completa e pode ser instalado sem uma base anterior. Também consegui demonstrar que o PatchDL produz um registro diferente da instalação direta: sem o marcador `fake`, com o CRC e com as partes representadas como numa atualização normal.

Nada disso concede o entitlement da PlayStation Store. Ativação offline e simulação do estado de login são operações diferentes de possuir a licença associada a este Content ID.

Na prática, “gratuito” não significa “sem licença”. ASTRO's PLAYROOM continua sendo um caso especial, provisionado pelo próprio sistema, e não um modelo seguro para outros jogos gratuitos de PS5.

Não pretendo repetir automaticamente este experimento em cada título gratuito. Ainda vale preservar seus pacotes como artefatos históricos, mas, para uma conta que nunca passou pela PSN, a execução provavelmente ficará bloqueada no mesmo ponto.

Guardei no repositório apenas os pequenos metadados e o relato comparativo. O PKG, licenças, dados de conta e URLs diretas de distribuição não são publicados.

#ps5 #silent-hill #retail-pkg #patchdl #preservacao
