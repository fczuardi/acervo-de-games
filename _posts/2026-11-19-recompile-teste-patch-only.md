---
title: "Recompile — o teste patch-only revelou uma versão mais nova no disco"
date: 2026-11-19 17:55:00 -0300
---

Comprei uma cópia física da edição limitada de *Recompile* para PS5, `PPSA03183`. O disco ainda não tinha sido inserido neste console. Eu pretendia repetir, com um controle melhor, o teste patch-only que fiz com *Demon's Souls*: instalar primeiro o retail patch oficial, tentar abrir sem mídia e só depois usar o disco como licença local.

O resultado foi mais interessante do que a hipótese. O patch foi instalado sozinho, mas o disco não serviu apenas como licença. Ele contém `01.005.000`, uma revisão mais nova que o `01.004.000` listado como atualização mais recente pelo ProsperoPatches. O que eu tratava como update era, para esta prensagem, uma versão anterior.

## O patch 01.004.000 preservado

Baixei o manifesto original e montei o retail PKG com o [`fetchpkg`](https://github.com/ps5-payload-dev/fetchpkg), no commit `10c9bb95f651d594ba254c104ac96d0bc836ed2d`. O manifesto descreve duas partes contíguas, sem lacunas ou sobreposições:

- tamanho final: 1.604.976.640 bytes;
- primeira parte: 1.553.006.592 bytes;
- segunda parte: 51.970.048 bytes;
- manifesto: 1.067 bytes, SHA-256 `752bbb8efbd0738c305dd2441738f2ef04833ae5a87bde65231e5e38650734e8`;
- PKG montado: SHA-256 `b7f4e3994d9a193017a3bd4d70728c153d795bbf91e562fdf6f1a71510679127`.

As duas partes foram verificadas individualmente pelos SHA-256 declarados pela Sony. O conjunto de preservação contém o manifesto original, o registro de aquisição, o relatório por partes, a verificação integral e checksums agregados. As URLs de distribuição permanecem no acervo privado.

## Instalação antes do primeiro contato com o disco

O PatchDL normalmente só mostra jogos já conhecidos pelo console. Como *Recompile* nunca havia sido instalado, copiei o PKG preservado para `/data/patchdl/PPSA03183/` e reproduzi o pequeno `state.json` de um download órfão concluído, método que eu já tinha usado no experimento com *SILENT HILL: The Short Message*.

O scanner de downloads órfãos também exigia que o PKG tivesse o nome derivado do manifesto, `UP1309-PPSA03183_00-RECOMPILE0000000.pkg`. Depois desse ajuste, o card apareceu como **Não instalado**. O PatchDL obteve o manifesto e o CRC, instalou o pacote e manteve o PKG porque a exclusão automática estava desligada.

O monitoramento por FTP registrou a instalação:

- 20:40:48: `/user/app/PPSA03183`, `/user/patch/PPSA03183` e `/user/appmeta/PPSA03183` ausentes;
- 20:41:01: `appmeta` presente;
- 20:41:14: `/user/app/PPSA03183` presente;
- `/user/patch/PPSA03183` permaneceu ausente.

O `app.pkg` instalado tinha os mesmos 1.604.976.640 bytes do arquivo preservado. Sem o disco, a tentativa de execução foi recusada antes do jogo abrir: o sistema informou que não podia usar o conteúdo nem se conectar ao servidor para verificar a licença.

## O disco não era a versão esperada

Ao inserir o disco pela primeira vez, o PS5 não o aceitou apenas como licença para a instalação existente. Em vez disso, informou que já havia outra versão instalada e ofereceu reinstalar do disco, cancelar ou atualizar. A opção de atualização levou a uma segunda tela de erro, com apenas reinstalação ou cancelamento. Cancelei as duas operações; os arquivos da instalação patch-only permaneceram inalterados.

Depois escolhi a reinstalação completa pelo disco. O console removeu `app`, `appmeta` e a instalação patch-only, recriou os metadados e copiou a aplicação física. A inspeção do novo `param.json` revelou:

- Content Version: `01.005.000`;
- Master Version: `02.00`;
- Content ID: `UP1309-PPSA03183_00-RECOMPILE0000000`.

O pacote do disco também é materialmente diferente do patch:

| | Disco `01.005.000` | Patch `01.004.000` |
|---|---:|---:|
| Tamanho total | 1.605.435.392 | 1.604.976.640 |
| Parte principal | 1.553.465.344 | 1.553.006.592 |
| Parte SC | 51.970.048 | 51.970.048 |
| Package digest | `93E8D737…F3917C` | `09B42025…58ACC` |
| CRC digest | `59327AA5…970DF` | `AC9CA246…3ED99` |

O ProsperoPatches lista `01.000.000`, `01.002.000`, `01.003.000` e `01.004.000` para esse Title ID, mas não `01.005.000`. Isso não demonstra que a revisão seja exclusiva desta edição: o site cataloga updates publicados no CDN, não necessariamente todas as revisões prensadas em disco. Ainda assim, esta cópia física da edição limitada contém inequivocamente uma master posterior à atualização pública preservada. A embalagem especial pode coincidir com uma prensagem posterior, mas os dados disponíveis não bastam para afirmar que todas as cópias da edição limitada usem a mesma master.

## Dump e imagem de trabalho

Com `01.005.000` instalado pelo disco e executando normalmente, fiz uma extração FLAT com o PS5 App Dumper v2.10. A descriptografia ficou ligada; FSELF e backport, desligados. O `dump-info.json` registra estado `done`, 2.839.878.696 bytes processados e conclusão da descriptografia sem erro.

Depois de incorporar a árvore ao acervo, gerei os manifestos pelo protocolo atual:

- 176 arquivos regulares;
- 2.801.195.414 bytes aparentes;
- SHA-256 do manifesto de arquivos: `f15d72af52c5651e1bdeb39ca2decd349226999709c77e749ae4f95c9382fb75`;
- SHA-256 do manifesto de tamanhos: `dc2593919fd1f5bfa9a7bad09a4e6ba605e575143cf6c7507e25248d5518e5de`.

Também criei com o Dump Forge uma imagem derivada de 1.956.904.960 bytes. Seu SHA-256 é `4e0cedc9ee2b2d9e4e7580be284df8c7e43314789fd61d4c69e1ebdf87cc38b0`. O ShadowMount registrou essa imagem a partir do M.2 como `PPSA03183`, versão `01.005.000`, sem reinstalar um `app.pkg` nativo. A validação de execução sem o disco ainda precisa ser registrada; por isso a imagem permanece como working copy em conferência, não como ciclo concluído.

## Resultado

O experimento patch-only não repetiu o comportamento de *Demon's Souls*. O `01.004.000` oficial é instalável como aplicação completa, mas não abre sem licença e não combina com este disco, que carrega a revisão posterior `01.005.000`. O prompt de versão diferente não indicava um patch defeituoso: revelava uma versão física ausente do histórico público consultado.

O resultado muda a prioridade de preservação. O dump do disco `01.005.000` e sua identificação como Master Version `02.00` são agora os artefatos centrais; o patch `01.004.000` continua preservado como revisão histórica anterior. A working copy só será marcada como validada depois de um teste de execução sem o disco.

#ps5 #recompile #patchdl #patch-only #midia-fisica #preservacao
