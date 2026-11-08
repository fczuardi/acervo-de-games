---
title: "Protocolo para dump de referência v0.1.0"
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
3. Reiniciar o aparelho e entrar com uma conta local sem histórico de uso.
4. Inserir o disco e aguardar a conclusão da instalação.
5. Registrar a versão do jogo instalada e verificar se há conteúdo ainda pendente de instalação.
6. Executar o PS5 App Dumper com as configurações acima.
7. Registrar os detalhes do dump: nome da pasta, tamanho, quantidade de arquivos e hashes de alguns arquivos selecionados.
8. Opcionalmente, preservar o log do processo, removendo informações pessoais, identificadores específicos do console e outros dados sensíveis antes da publicação.

## Limitações

O resultado representa os arquivos extraídos da instalação offline pelo PS5 App Dumper, não uma imagem óptica integral do disco.

A reprodutibilidade dos hashes entre consoles diferentes ainda precisa ser verificada.

#ps5 #dump
