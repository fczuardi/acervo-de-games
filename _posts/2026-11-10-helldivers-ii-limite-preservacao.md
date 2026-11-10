---
title: "Helldivers II e o limite do que consigo preservar"
date: 2026-11-10 10:30:00 -0300
---

Enquanto baixava a atualização `01.007.101` de Helldivers II, a mais recente que encontrei compatível com meu PS5 no firmware 13.60, fiquei pensando no que exatamente significa preservar este jogo.

A ideia inicial era seguir o mesmo processo dos outros discos do lote: instalação limpa, dump da versão base, manifestos de arquivos e tamanhos, preservação do retail PKG, instalação do update, novo dump e uma cópia de trabalho separada. Tudo isso continua tendo valor como registro do software que foi lançado: executáveis, assets, menus, telas, mensagens e as diferenças entre versões.

Mas Helldivers II praticamente não tem um jogo offline escondido ali dentro.

O [teste do DoesItPlay](https://www.doesitplay.org/game/Helldivers%202/ps5/Base%20PS5?region=ESRB&version=Standard) classifica a edição física de PS5 como sem jogo offline e com download obrigatório. Segundo o relato, sem conexão ela nem chega a um menu, apenas mostra uma mensagem de falha. A [metodologia do site](https://www.doesitplay.org/methodology) usa instalação nova, console inteiramente offline e um perfil que nunca acessou a PSN. É uma referência muito próxima do teste que eu faria, mas não substitui a observação do meu próprio disco.

No meu caso existe ainda uma escolha pessoal: eu me comprometi a não voltar para a PSN. Se quiser jogar Helldivers II com amigos, provavelmente terei que comprar outra cópia no PC. O exemplar de PS5 fica com outro papel. Ele é um objeto de preservação, mesmo que eu nunca consiga usá-lo como jogo completo.

## O disco do primeiro Helldivers

Tenho também uma edição física brasileira do primeiro Helldivers para PS4. Aproveitei esta reflexão para começar o inventário dela pelas informações visíveis na caixa, no disco e no encarte:

| Campo | Valor observado |
|---|---|
| Título | Helldivers — Edição Final do Super-Earth |
| Product code | `CUSA-02945` |
| Identificador na lombada | `3001195` |
| Identificador acima do código de barras | `3001195-AC` |
| Identificador do disco | `3001195-DL` |
| Código de barras | `7 11719 50256 2` |
| Classificação indicativa | 12 anos — Violência |

A embalagem anuncia edições para PS4, PS3 e PS Vita, todas as expansões, 11 pacotes de conteúdo para download, um pacote de armas bônus e um tema dinâmico para PS4. O código incluído para acrescentar conteúdo por download tem data de validade de 18 de agosto de 2018.

A presença do voucher e de uma validade própria é uma evidência forte de que pelo menos parte da edição dependia de um entitlement da PSN, não apenas do disco. Ainda não sei quais itens estão efetivamente gravados na mídia e quais eram concedidos pelo código. Isso só poderá ser separado com uma instalação limpa e completamente offline, seguida pela inspeção do disco e do resultado instalado.

É um problema diferente do segundo jogo. O primeiro Helldivers pode preservar no disco uma experiência local funcional, enquanto a completude da edição comercial depende de downloads que expiraram. Em Helldivers II, o próprio funcionamento do cliente como jogo depende do serviço.

## O cliente e o serviço

Uma cópia executável do cliente não preserva automaticamente:

- autenticação e identidade;
- matchmaking e formação de grupos;
- progressão, inventário e recompensas;
- estado da Guerra Galáctica;
- ordens, campanhas e mensagens operadas pela Arrowhead;
- validação do resultado das missões;
- a parte da simulação que eventualmente exista apenas no backend.

Ainda não sei sequer onde termina a comunicação entre jogadores e onde começa o serviço central. O cross-play com PC mostra que há infraestrutura compartilhada, mas não demonstra que o cliente de PS5 possa utilizá-la sem passar pela PSN.

Para este jogo, uma working copy validada talvez significasse somente que o dump foi montado, o cliente abriu sem o disco e chegou corretamente até sua barreira de rede. Registrar a tela alcançada, a mensagem exibida e as diferenças entre o cliente base e o atualizado ainda seria um resultado verificável, mas bem menor que jogar.

## O que já existe na comunidade

Uma busca inicial encontrou o projeto aberto [helldivers-2/api](https://github.com/helldivers-2/api), que mantém uma API comunitária e uma descrição OpenAPI da superfície usada para consultar dados da Arrowhead. A comunidade já consegue acompanhar planetas, campanhas, ordens e o estado corrente da guerra.

É uma peça interessante da preservação do serviço, mas não é um servidor comunitário do jogo. A API consulta e reorganiza dados do backend ainda existente. Ela não se apresenta como substituta para autenticação, matchmaking, sessões, progressão ou execução de missões.

Não encontrei, nesta primeira pesquisa, um projeto público capaz de receber o cliente retail de PS5 ou PC e substituir o backend completo. Isso não prova que não exista trabalho privado ou experimental. Significa apenas que ainda não tenho uma implementação verificável para apontar.

Um futuro servidor comunitário provavelmente exigiria, entre outras coisas, entender:

1. como o cliente obtém identidade e autorização na PSN ou no Steam;
2. quais serviços são compartilhados entre as plataformas;
3. como endpoints e certificados poderiam ser substituídos;
4. quais mensagens cuidam de lobby, matchmaking e sessões;
5. o que fica sob responsabilidade do host da partida e o que depende do backend;
6. como são representados progressão, equipamentos, ordens e o estado da guerra;
7. quais verificações de versão e integridade impedem clientes antigos de entrar.

Esta lista é um mapa de perguntas, não uma descrição confirmada da arquitetura de Helldivers II. Preservar versões exatas do cliente, seus metadados e seu comportamento pode ajudar uma pesquisa futura, mas não resolve sozinho nenhuma dessas camadas.

## Uma proposta de fim de vida

No Brasil está em tramitação o [PL 3612/2026](https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2638495), apresentado pela deputada Jandira Feghali. O projeto trata da proteção de compradores de jogos eletrônicos e da preservação do patrimônio cultural digital.

Segundo o [resumo publicado pela Câmara](https://www.camara.leg.br/noticias/1294146-projeto-estabelece-que-jogos-eletronicos-continuem-mesmo-apos-desligamento-de-servidores), a proposta exige prazo mínimo de suporte, aviso prévio antes do encerramento e pelo menos uma entre três alternativas: uma versão offline, ferramentas que permitam a manutenção pela comunidade ou ressarcimento parcial. O texto também prevê a possibilidade de servidores comunitários depois do fim do serviço oficial.

Há uma ressalva importante: como as alternativas aparecem dessa forma, a aprovação não significaria necessariamente que toda empresa teria que publicar um servidor ou documentação técnica. O ressarcimento poderia ser a saída escolhida. Ainda assim, reconhecer em lei que o fim unilateral de um servidor precisa de uma política de saída já seria uma mudança grande.

Em 10 de novembro de 2026, o projeto ainda não é lei. A ficha da Câmara informa regime de urgência e aguarda designação de relatoria na Comissão de Ciência, Tecnologia e Inovação, além da tramitação pelas demais comissões indicadas.

## Onde parei por enquanto

Depois desta pesquisa, decidi não fazer agora os dumps base e atualizado nem uma working copy de Helldivers II. Há outros jogos mais autônomos e jogáveis na fila, e cada uma dessas etapas ocupa horas. O disco continua no inventário e posso retomar o experimento no futuro.

Nesta etapa preservei o manifesto de distribuição e o retail PKG `01.007.101`, a versão mais recente que encontrei compatível com meu firmware. O pacote tem 40.628.846.592 bytes, distribuídos em 11 partes descritas pelo manifesto da Sony.

Calculei o SHA-256 do pacote completo e verifiquei as 11 faixas na mesma leitura. Todas coincidiram com os hashes do manifesto:

```text
6a7a7d2fb2d7c4668dacfe3ccf9f98fd39ba9fdfdd0415efcc2bd48500272d3a
```

O campo `packageDigest` do manifesto, `8CF045122E8001C6DCF7503FD0EBF0CB3BF04DC72B096139FE2E91756BB1E70D`, novamente não corresponde ao SHA-256 do PKG montado. Preservei separadamente o registro da aquisição, o relatório por parte e o resumo da verificação.

Este é um limite consciente de escopo, não uma conclusão de que o cliente não merece ser preservado. Se um dia existirem ferramentas oficiais de fim de vida ou uma implementação comunitária do serviço, os clientes exatos poderão ganhar uma utilidade nova. Por enquanto, prefiro dedicar o tempo aos exemplares da coleção que consigo salvaguardar e usar de maneira mais completa.

#ps5 #helldivers-ii #preservacao #live-service #servidores
