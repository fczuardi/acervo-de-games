---
title: "O que preservar de uma atualização oficial de PS5"
date: 2026-11-09 08:41:00 -0300
---

Ao preservar a atualização `01.007.000` de Demon's Souls, percebi que o PKG retail e seu manifesto de distribuição são artefatos diferentes do dump descriptografado do jogo e também merecem ser guardados.

O PKG oficial não é apenas um meio temporário para chegar à instalação atualizada. Mesmo que seu conteúdo principal não possa ser lido diretamente, ele registra a forma exata como a Sony distribuiu aquela versão.

## O manifesto de distribuição

Baixei a atualização com o [`fetchpkg`](https://github.com/ps5-payload-dev/fetchpkg), usando o manifesto JSON fornecido pela infraestrutura da Sony. Esse manifesto descreve como montar o pacote final a partir de várias peças.

No caso de Demon's Souls, ele informa:

- tamanho final de 53.805.318.144 bytes;
- 14 peças;
- offset e tamanho de cada peça;
- SHA-256 individual de cada peça;
- os campos `packageDigest` e `playgoChunkCrcHashValue`.

Os 14 intervalos são contínuos, sem lacunas ou sobreposições, e a soma dos tamanhos coincide com `originalFileSize`. Todos os hashes individuais foram verificados depois do download.

Preservei o JSON original. Como ele contém URLs diretas para arquivos de distribuição, não pretendo publicá-lo. Para identificar exatamente esse manifesto sem expor os endereços, registrei seu tamanho, 4.881 bytes, e seu SHA-256:

```
1fd9334099ae3f62f5f4f08ce4f58ca7935980475089bb33f6645f73ea627b63
```

## O PKG montado

O `fetchpkg` baixa as peças na ordem do manifesto, verifica o hash de cada uma e as escreve no arquivo de saída. O PKG montado de Demon's Souls tem SHA-256:

```
af8f4e109085b6e28ed53c9af6b23295443edc965aa095e7637770cf0e63b523
```

Esse valor não coincide com o `packageDigest` registrado pela Sony:

```
7199D8EE8C956C592BAB6DFFA44D7DDDBB2FA2E6933A0856844FBE468B7FE0E3
```

O código do `fetchpkg` não usa `packageDigest` para validar o download. Por enquanto, preservo o campo literalmente, mas sua semântica continua em aberto. Não é correto apresentá-lo como o SHA-256 do PKG completo.

## O que aparece sem descriptografia

Os primeiros dados do arquivo montado parecem opacos e não foram reconhecidos pelo comando `file`. Isso é compatível com um payload cifrado, mas, isoladamente, não é prova suficiente para descrever toda a estrutura criptográfica.

A última peça, porém, começa no offset `53.694.955.520` com a assinatura hexadecimal `7f 43 4e 54`, ou `.CNT`, e contém em claro o Content ID:

```
UP9000-PPSA01342_00-DEMONSSOULS00000
```

[Implementações abertas do formato](https://github.com/john-tornblom/LibProsperoPKG-seregonwar/blob/main/docs/ps5-pkg-format.md) descrevem o CNT como um contêiner de metadados e o PFS como a imagem cifrada e protegida por integridade que contém os arquivos da aplicação. Essa documentação vem de engenharia reversa e não deve ser confundida com uma especificação pública da Sony.

Também observei que as peças principais usam identificadores `JP9000-PPSA01339`, enquanto a peça final de metadados usa `UP9000-PPSA01342`. Isso pode indicar reaproveitamento de conteúdo entre regiões, mas ainda não investiguei o mecanismo e não considero essa explicação demonstrada.

## O que vale preservar

Para futuras atualizações oficiais, pretendo guardar separadamente:

- o manifesto original, sem alterações;
- o PKG retail montado;
- tamanho e SHA-256 dos dois arquivos;
- quantidade, offsets, tamanhos e hashes das peças;
- resultado da verificação local de cada peça;
- confirmação de continuidade dos intervalos e do tamanho final;
- campos fornecidos pela Sony cuja semântica ainda não esteja resolvida;
- versão ou commit e SHA-256 da ferramenta usada no download;
- data da obtenção e observações sobre a origem do manifesto;
- metadados legíveis do cabeçalho, quando puderem ser extraídos sem modificar o pacote.

O manifesto público pode ser uma versão derivada sem URLs, acompanhada do hash do JSON original preservado em privado.

## Artefatos diferentes

O PKG retail preserva a distribuição oficial cifrada. O dump feito depois da instalação preserva uma visão descriptografada dos arquivos montados pelo console. Um não substitui o outro.

No caso de Demon's Souls, mantive separados:

1. o manifesto de distribuição da Sony;
2. o PKG retail original montado a partir das 14 peças;
3. o dump descriptografado da instalação `01.007.000`.

A instalação offline e a chegada até a tela de seleção de idioma demonstraram que esse PKG foi aceito pelo console e que o jogo iniciou. Isso não demonstra jogabilidade completa, nem resolve todos os detalhes internos do formato.

#ps5 #pkg #patch #atualizacao #preservacao
