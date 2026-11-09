---
title: "Protocolo para dump de referência v0.3.0"
date: 2026-11-08 16:44:00 -0300
---

Objetivo: obter um dump de referência dos arquivos instalados a partir de um disco físico de PS5, sem atualizações baixadas da internet ou modificações destinadas à execução.

## Ambiente

- Leitor: PS5 com firmware 13.60
- Software: [PS5 App Dumper](https://github.com/EchoStretch/ps5-app-dumper), de EchoStretch
  - Versão: [v2.10 beta](https://github.com/EchoStretch/ps5-app-dumper/releases/tag/v2.10)
  - SHA-256 do arquivo da ferramenta: `c850f1df6f2787824d6ddeeed69ce4144e00569b32135973401c2985cfb0345b` (arquivo a identificar)

## Configuração do PS5 App Dumper

- Decrypt executables: ligado (preservar também os executáveis originais, quando disponíveis no dump)
- Write logs: ligado
- PS4 split mode: Both (não se aplica a jogos de PS5)
- Create FSELF files: desligado
- Dump DLC along: desligado
- Game title in folder names: ligado
- SDK backport: desligado

## Procedimento

1. Deletar qualquer instalação anterior do jogo, incluindo atualizações e DLCs.
2. Desconectar o PS5 da internet.
3. Reiniciar o aparelho e entrar na conta habitual para executar o jailbreak.
4. Inserir o disco e aguardar a cópia completa para o console, não apenas o estado "Pronto para jogar".
5. Registrar a versão do jogo instalada e confirmar que não há conteúdo pendente de instalação (inclusive verificar se o dumper ainda indica `INSTALLING`).
6. Abrir o jogo e aguardar a primeira tela interativa (por exemplo, ajuste de brilho, menu inicial ou "Press Start"), sem iniciar uma partida ou criar um save, se possível.
7. Deixar o jogo em execução e iniciar o dump pela interface do PS5 App Dumper com as configurações acima.
8. Registrar os detalhes do dump: nome da pasta, tamanho aparente, quantidade de arquivos, metadados gerados pelo dumper e hashes de alguns arquivos selecionados.
9. Opcionalmente, preservar o log do processo, removendo informações pessoais, identificadores específicos do console e outros dados sensíveis antes da publicação.

## Manifestos de integridade e tamanho

Depois do dump, gerar e preservar dois manifestos ao lado da pasta extraída, sem criar arquivos dentro dela:

- um manifesto SHA-256, com o hash e o caminho relativo de cada arquivo regular;
- um manifesto TSV, com o tamanho aparente em bytes e o caminho relativo dos mesmos arquivos.

Os dois manifestos excluem `sce_sys/`. Essa pasta pode incluir metadados copiados de áreas do sistema pelo dumper e, por precaução, não faz parte do conjunto público de referência.

Executar os comandos a partir da raiz da pasta extraída. Para o manifesto SHA-256:

```bash
find . -type f \
  ! -path './sce_sys/*' \
  -print0 |
  LC_ALL=C sort -z |
  xargs -0 -r sha256sum \
  > ../TITLE-VERSION.sha256
```

Antes de escolher TSV para os tamanhos, verificar os nomes com uma leitura delimitada por NUL. Se algum caminho contiver tabulação ou quebra de linha, não gerar um TSV ambíguo: usar uma representação delimitada por NUL e documentar a exceção.

```bash
find . -type f \
  ! -path './sce_sys/*' \
  -print0 |
  perl -0ne '
    $files++;
    $tabs++     if /\t/;
    $newlines++ if /\n/;
    END {
      print "files=$files tabs=" . ($tabs || 0) .
            " newlines=" . ($newlines || 0) . "\n";
    }
  '
```

Se não houver tabulações nem quebras de linha, gerar um TSV sem cabeçalho no formato `tamanho_em_bytes<TAB>./caminho/relativo`:

```bash
set -o pipefail

find . -type f \
  ! -path './sce_sys/*' \
  -printf '%s\t%p\0' |
  LC_ALL=C sort -z -t $'\t' -k2,2 |
  tr '\0' '\n' \
  > ../TITLE-VERSION.sizes.tsv
```

Calcular e registrar os hashes dos próprios manifestos:

```bash
sha256sum \
  ../TITLE-VERSION.sha256 \
  ../TITLE-VERSION.sizes.tsv
```

Verificar que ambos têm a mesma quantidade de entradas e exatamente o mesmo conjunto ordenado de caminhos. Essa verificação deve usar um parser adequado ao formato de saída do `sha256sum`, inclusive suas regras de escape. Não se deve extrair o caminho por uma posição fixa na linha: quando um nome contém certos caracteres especiais, como barra invertida, o `sha256sum` pode escapar o nome e alterar o formato aparente da linha.

Também registrar a soma dos tamanhos aparentes incluídos:

```bash
awk -F '\t' '
  { total += $1 }
  END { printf "%.0f\n", total }
' ../TITLE-VERSION.sizes.tsv
```

O manifesto de tamanhos permite calcular o volume exato de arquivos adicionados ou substituídos entre versões sem reler o conteúdo integral dos dumps. Ele registra tamanhos aparentes, não o espaço alocado no sistema de arquivos.

## Limitações

O resultado representa os arquivos extraídos da instalação offline pelo PS5 App Dumper, não uma imagem óptica integral do disco.

A reprodutibilidade dos hashes entre consoles diferentes ainda precisa ser verificada.

## Alterações na v0.3.0

- O manifesto SHA-256 passa a fazer parte explícita do protocolo.
- Foi acrescentado um manifesto permanente de tamanhos aparentes.
- Os dois manifestos usam a mesma exclusão de `sce_sys/` e ordenação determinística por caminho.
- Foi acrescentada a verificação de nomes incompatíveis com TSV e da equivalência dos caminhos entre os manifestos.

#ps5 #dump
