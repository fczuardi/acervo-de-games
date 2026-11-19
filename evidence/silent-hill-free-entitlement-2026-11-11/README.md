# Experimento de licença — SILENT HILL: The Short Message

Evidências textuais do experimento realizado em 11 de novembro de 2026 com
`SILENT HILL: The Short Message` (`PPSA04877`), versão `01.000.001`, num PS5
com firmware `13.60` mantido fora da PSN.

O objetivo foi separar três perguntas:

1. o retail patch oficial pode ser instalado sem um jogo-base;
2. o método de instalação muda o registro local da aplicação;
3. uma instalação completa permite executar o jogo numa conta sem histórico
   de aquisição na PSN.

## Retail patch preservado

- tamanho: `12148146176` bytes;
- SHA-256: `2330b9dab40a0a2cbfba03931459116bca946a616f6e588cc643c5bc70fcfd3c`;
- manifesto SHA-256:
  `f3c34cad7919c363fcb3d9df1ced1c1feb9a7a94f75b00e4647e074db407ae4b`;
- peças verificadas contra o manifesto Sony: `4/4`;
- versão mínima de firmware informada pela fonte: `08.20.00.06`.

O PKG e seus registros completos de aquisição e verificação permanecem fora
do repositório.

## Instalação direta

O PKG foi instalado sem jogo-base pelo PS5 Web File Manager. A instalação
terminou e foi marcada como pronta para jogar. O resultado ficou em
`/user/app/PPSA04877/`, sem `/user/patch/PPSA04877/`.

O `app.json` resultante tinha 336 bytes, registrava uma única peça apontando
para o PKG no USB e continha `"fake":true`. Não foi observado `app.crc` nessa
instalação.

Ao executar, o shell recusou o conteúdo antes de iniciar o jogo:

```text
Can't use this content.
Can't connect to the server to verify your license. Wait a while and then try again.
```

Os metadados observados permaneceram byte a byte iguais após a tentativa.

## Instalação pelo PatchDL

O PatchDL v0.3.12 não oferece normalmente o jogo quando ele está ausente e
também não oferece baixar novamente a única versão quando ela já está
instalada. Para testar somente sua rotina de instalação, o PKG preservado foi
adotado manualmente como um download órfão completo em
`/data/patchdl/PPSA04877/`.

O estado manual reproduziu o formato que o próprio PatchDL grava: Title ID,
URL do manifesto, versão, nome, tamanho, quatro peças concluídas e nenhum
fragmento parcial. Ao reiniciar, o PatchDL mostrou o título como não instalado
e ofereceu **Instalar 01.000.001**.

A instalação terminou e foi marcada como pronta para jogar. Desta vez:

- `app.json` tinha 1004 bytes e não continha `"fake":true`;
- as quatro peças do manifesto Sony foram registradas com URLs locais do
  PatchDL em `127.0.0.1:12880`;
- `app.crc` foi instalado com 741464 bytes;
- o `app.pkg` continuou com 12148146176 bytes;
- `/user/patch/PPSA04877/` permaneceu ausente;
- os dois appmeta `param.json` foram byte a byte iguais aos da instalação
  direta.

A execução foi recusada com exatamente a mesma mensagem de licença. Os
metadados observados também permaneceram inalterados após essa tentativa.

## Resultado

O retail patch contém uma aplicação completa e instalável. O método PatchDL
produz um registro diferente e mais próximo do fluxo normal de atualização,
sem o marcador `fake`, mas isso não concede o entitlement necessário para
executar o jogo.

Neste caso, ativação técnica, CRC e formato do `app.json` são independentes da
licença associada à conta. O experimento não demonstra que todo jogo gratuito
tenha o mesmo comportamento, mas fornece um caso de referência suficiente
para não repetir automaticamente o procedimento em cada título da PS Store.

Nenhum PKG, licença, save, identificador de conta ou URL direta de distribuição
é publicado aqui.
