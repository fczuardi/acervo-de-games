---
title: "Astro Bot — segunda aplicação do protocolo patch-first"
date: 2026-11-21 21:45:00 -0300
---

*Astro Bot* para PS5 (`PPSA21564`) é o segundo jogo ao qual aplico o protocolo
experimental v0.4.0. O método, testado primeiro com *Elden Ring*, inverte a
ordem habitual: instala o retail update oficial antes da base, tenta executar
essa aplicação completa usando o disco somente como licença e deixa a
instalação limpa da mídia para o fim.

O objetivo não é recomendar o patch-only como forma normal de instalação. O
experimento verifica se o retail update preservado contém uma aplicação
autônoma, se o PS5 aceita a mídia física como licença local e se essa rota
produz um dump atualizado reproduzível sem depender primeiro da cópia do
disco.

## Protocolo v0.4.0

Esta segunda aplicação segue as mesmas etapas definidas no estudo anterior:

1. preservar o manifesto e o retail update mais recente compatível com o
   firmware `13.60`;
2. criar o estado mínimo que faz o PatchDL listar um título ausente;
3. instalar apenas o patch, sem uma base já registrada;
4. inserir o disco como licença local e testar a execução;
5. extrair o jogo atualizado;
6. produzir, verificar, fingerprintar e testar uma working copy FFPKG;
7. remover a instalação atualizada;
8. instalar e extrair somente a versão-base do disco;
9. fingerprintar o dump-base;
10. substituir o payload do dump atualizado por um tombstone somente depois
    de todos os controles.

## Retail update 01.019.000

O update oficial preservado é `01.019.000`, requer firmware `13.20` e possui
37.886.558.208 bytes. O manifesto Sony descreve dez partes contíguas, todas
verificadas, e o retail PKG montado tem SHA-256
`783209ccdd6613b01522f7b257324be14e84cf143cf1a11efa1a26c51f4b578b`.

O conjunto foi reorganizado de acordo com a nova convenção do acervo. Existe
uma única cópia do arquivo grande, já no formato esperado pelo PatchDL:

```text
Astro Bot - PPSA21564/
└── PPSA21564/
    ├── UP9000-PPSA21564_00-0000000000000000.pkg
    └── state.json
```

Os manifestos, registros de aquisição, verificação por partes e checksums
agregados permanecem no diretório do jogo. Dessa forma, a conveniência de
instalação não exige uma segunda cópia do PKG.

## Instalação patch-only e licença do disco

Com *Astro Bot* ausente do console e o disco ejetado, copiei a pasta
`PPSA21564` para `/data/patchdl/`. O PatchDL apresentou o título com a ação de
instalação e entregou o retail PKG ao instalador nativo. A instalação de
`01.019.000` terminou sem uma base anterior.

Depois inseri o disco. A aplicação patch-only abriu normalmente, confirmando
o ponto central desta etapa: também neste jogo a mídia física pôde servir como
licença local para a revisão mais nova instalada a partir do retail update.

## Estado observado antes do dump

Uma leitura por FTP, feita enquanto o dump atualizado já estava em andamento,
mostrou:

- `/user/app/PPSA21564`: presente;
- `/user/patch/PPSA21564`: ausente;
- `/user/appmeta/PPSA21564`: presente;
- `app.pkg`: 37.886.558.208 bytes;
- versão instalada: `01.019.000`;
- Master Version: `01.00`;
- firmware mínimo codificado: `0x1320000000000000`;
- `/data/patchdl/PPSA21564`: preservado com o PKG e o estado concluído.

O `app.json` da instalação e o manifesto local do PatchDL concordam no tamanho,
nas dez partes, no `packageDigest` e no hash dos CRCs PlayGo. O `state.json`
registra os 37.886.558.208 bytes concluídos e o bitmap `ff03`, correspondente
às dez partes presentes. O snapshot completo está em
[`pre-dump-patch-only-state.txt`]({{ '/evidence/astro-bot-patch-first-2026-11-21/pre-dump-patch-only-state.txt' | relative_url }}).

## Estado atual

O dump de `01.019.000` foi concluído com o PS5 App Dumper v2.10 enquanto o
disco permanecia inserido e o jogo estava montado. O `dump-info.json` registra
estado `done`, 159.802.745.004 bytes processados, descriptografia ligada e
FSELF e backport desligados. O intervalo registrado no sidecar foi de 2h17m51s.

Houve uma primeira tentativa que deixou de registrar progresso em 68%, sem
mensagem explícita de erro ou cancelamento. A execução definitiva chegou a
148,77/148,77 GB e 100%; o log global registra em seguida o processamento de
appmeta, troféus e UDS, a descriptografia bem-sucedida e a conclusão do fluxo.
O estado pós-dump e o resumo dos dois logs estão em
[`post-dump-state.txt`]({{ '/evidence/astro-bot-patch-first-2026-11-21/post-dump-state.txt' | relative_url }}).

No PC, o Dump Forge v0.5.6 produziu uma working copy FFPKG com pacotes
Zstandard medium e verificação completa. A imagem possui 45.609.320.448 bytes
e SHA-256
`73b2cacf3dff4631f45c7b4e1cbf74182b93643259e525bdfe5c77f3f56887c9`.
Depois de copiada para o HD, ela foi montada pelo ShadowMount e executada sem
o disco, sem problema visível. A working copy e seu fingerprint estão,
portanto, concluídos.

O fingerprint do dump atualizado registra 166.700 arquivos e
159.744.132.637 bytes aparentes fora de `sce_sys/`. Os hashes dos manifestos
SHA-256 e de tamanhos são, respectivamente,
`e37d268371b295af824d057311657b632085ea3ea67569287e3d17fdc19f1fb2` e
`50be9d898337572c82ed891ea869e1a9089509f29a11372ac649969c8e1b3096`.

Por fim, removi a instalação atualizada, fiz a instalação limpa do disco e
extraí a versão-base `01.000.000`. O sidecar registra estado `done`,
154.993.980.216 bytes processados e as mesmas opções conservadoras do dump
atualizado. Seu fingerprint contém 146.987 arquivos e 154.935.393.869 bytes
aparentes; os hashes dos manifestos SHA-256 e de tamanhos são
`9d885b865c16cc0dbef9de48b9672871a78824d6eeb8a1b631dcbac2c5d9876b` e
`b1182267b27c65e8c34e681747d8bbfa68b695ac3e418130ed3e91f174981815`.

Com isso, todas as etapas obrigatórias desta aplicação do protocolo estão
concluídas. O payload do dump atualizado foi substituído por um tombstone,
mantendo os dois manifestos, o sidecar e o registro da working copy. O
dump-base permanece integral.

O acervo também conserva o tombstone do dump intermediário `01.018.000`. Essa
revisão continua historicamente identificada por seus manifestos, mas não será
confundida com o novo dump de referência atualizado `01.019.000`.

#ps5 #astro-bot #patchdl #patch-only #protocolo #preservacao
