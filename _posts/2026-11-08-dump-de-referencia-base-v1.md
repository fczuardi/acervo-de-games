---
title: "Protocolo para dump de referência v0.2.1"
date: 2026-11-08 16:44:00 -0300
---

Objetivo: obter um dump de referência dos arquivos instalados a partir de um disco físico de PS5, sem atualizações baixadas da internet ou modificações destinadas à execução.

## Ambiente

- Leitor: PS5 com firmware 13.60
- Software: [PS5 App Dumper](https://github.com/EchoStretch/ps5-app-dumper), de EchoStretch
  - Versão: [v2.10 beta](https://github.com/EchoStretch/ps5-app-dumper/releases/tag/v2.10)
  - SHA-256 do arquivo da ferramenta: `c850f1df6f2787824d6ddeeed69ce4144e00569b32135973401c2985cfb0345b` (arquivo a identificar)

## Configuração do PS5 App Dumper

- FSELF: desligado
- Auto backport: desligado
- Dump DLC: desligado

## Procedimento

1. Deletar qualquer instalação anterior do jogo, incluindo atualizações e DLCs.
2. Desconectar o PS5 da internet.
3. Reiniciar o aparelho e entrar na conta habitual para executar o jailbreak.
4. Inserir o disco e aguardar a cópia completa para o console, não apenas o estado "Pronto para jogar".
5. Registrar a versão do jogo instalada e confirmar que não há conteúdo pendente de instalação (inclusive verificar se o dumper ainda indica `INSTALLING`).
6. Abrir o jogo e aguardar a primeira tela interativa (por exemplo, ajuste de brilho, menu inicial ou "Press Start"), sem iniciar uma partida ou criar um save, se possível.
7. Deixar o jogo em execução e iniciar o dump pela interface do PS5 App Dumper com as configurações acima.
8. Registrar os detalhes do dump: nome da pasta, tamanho, quantidade de arquivos e hashes de alguns arquivos selecionados.
9. Opcionalmente, preservar o log do processo, removendo informações pessoais, identificadores específicos do console e outros dados sensíveis antes da publicação.

## Limitações

O resultado representa os arquivos extraídos da instalação offline pelo PS5 App Dumper, não uma imagem óptica integral do disco.

A reprodutibilidade dos hashes entre consoles diferentes ainda precisa ser verificada.

#ps5 #dump
