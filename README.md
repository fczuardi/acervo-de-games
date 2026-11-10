# Acervo de Games

Diário público de atividades de preservação de jogos. Sem disponibilização de jogos para download.

O site lista entradas Markdown em ordem cronológica reversa, gerado com Jekyll no GitHub Pages.

Para publicar um registro, crie um arquivo em `_posts/` com nome `AAAA-MM-DD-titulo.md`:

```markdown
---
layout: null
title: Título do registro
date: 2026-11-08
---

Texto do registro.
```

O layout de cada entrada será definido quando publicarmos a primeira. O objetivo inicial é registrar atividades sem estrutura obrigatória.

## Ferramentas locais

O `Justfile` reúne comandos repetidos durante o trabalho de preservação. Para baixar um patch com o `fetchpkg`, sem sobrescrever silenciosamente um arquivo anterior:

```bash
just download-patch /caminho/fetchpkg /caminho/manifest.json /destino/patch.pkg 'URL'
```

O download é gravado primeiro como `patch.pkg.part`. Como o `fetchpkg` não retoma downloads interrompidos, a receita recusa arquivos parciais ou finais preexistentes. Depois do sucesso, ela confere o tamanho contra o manifesto, renomeia o arquivo e cria `patch.acquisition.json` com metadados da aquisição e da ferramenta, mas sem reter a URL completa.

Para calcular o SHA-256 completo de um retail PKG e verificar todas as partes descritas no manifesto da Sony durante a mesma leitura sequencial:

```bash
just verify-patch "/caminho/da/pasta-do-jogo" nome-base-do-patch
```

O comando espera arquivos chamados `nome-base-do-patch.json` e `nome-base-do-patch.pkg`. Se o tamanho, o layout ou qualquer hash de parte divergir, ele termina sem gravar resultados. Quando tudo confere, cria:

- `nome-base-do-patch.pieces.sha256.tsv`;
- `nome-base-do-patch.verification.json`.

Os scripts não contêm jogos, chaves, URLs de distribuição ou outros dados do acervo privado.
