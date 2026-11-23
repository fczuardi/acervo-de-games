---
title: "Plano: um índice público de integridade para patches retail de PS5"
date: 2026-11-23 12:00:00 -0300
---

Este é um plano para um projeto futuro, não o anúncio de uma coleção já
publicada. A ideia nasceu de uma fragilidade observada durante a preservação
dos patches retail de PS5: hoje ainda consigo baixar as peças originais da CDN
da Sony, mas não há garantia de que esses objetos permanecerão disponíveis, e
os principais catálogos públicos preservam sobretudo metadados e links, não
uma segunda cópia dos payloads.

Em vez de publicar os retail PKGs, quero estudar a criação de um índice público
de proveniência e integridade. Ele permitiria identificar precisamente cada
patch, verificar uma cópia obtida por meios legítimos e reconstruir o PKG
enquanto as peças oficiais ainda existirem, sem redistribuir o jogo ou o patch.

## Limite público e privado

O acervo local continuará contendo os artefatos grandes necessários ao meu
trabalho de preservação. A exportação pública será uma visão sanitizada e
baseada em uma lista explícita do que pode sair.

Podem entrar na exportação:

- manifesto SC original e seu checksum;
- Title ID, Content ID, versão e firmware mínimo;
- URLs oficiais da CDN;
- offsets, tamanhos e hashes declarados para cada peça;
- tamanho e SHA-256 do retail PKG reconstruído;
- registros de aquisição e de verificação;
- `state.json` compatível com PatchDL;
- fingerprints de dumps já publicados como evidência textual;
- tombstones, documentação do protocolo e scripts de verificação.

Não podem entrar:

- retail PKGs ou suas peças;
- dumps descriptografados;
- working images;
- licenças, credenciais, cookies, tokens ou chaves;
- conteúdo extraído de `sce_sys/`;
- logs com IPs, nomes de usuário, caminhos pessoais ou outros identificadores;
- qualquer arquivo que não tenha sido aprovado pela regra de exportação.

A ausência de payloads é uma escolha técnica e jurídica deliberada. O projeto
descreverá arquivos e registrará sua integridade; não funcionará como mirror de
software PlayStation.

## Arquitetura proposta

A fonte continuará sendo o repositório privado de trabalho. Um exportador
reproduzível criará uma árvore pública nova, em vez de tentar remover arquivos
perigosos de uma cópia completa. A regra deve ser *allowlist*: somente extensões,
nomes e campos conhecidos serão copiados.

Antes de publicar, o exportador deverá:

1. recusar arquivos grandes e qualquer extensão de pacote ou imagem;
2. procurar segredos e identificadores pessoais;
3. normalizar ou remover caminhos locais;
4. validar todos os JSONs e manifestos;
5. recalcular checksums dos arquivos exportados;
6. produzir um inventário final com nome, tamanho e SHA-256;
7. falhar de forma fechada diante de qualquer arquivo desconhecido.

Também quero que cada registro deixe clara a proveniência: URL consultada,
data da aquisição, hash do manifesto, resultado da verificação por peças e
versão do script usado. Assim, outra pessoa poderá auditar o registro sem
precisar confiar apenas na minha descrição.

## Publicação e redundância

O primeiro destino pode ser um repositório Git público, adequado a arquivos
pequenos, texto, histórico de alterações e revisão comunitária. Snapshots
versionados desse repositório poderiam ser enviados periodicamente ao Internet
Archive como uma segunda camada de preservação.

O upload ao Internet Archive deverá conter somente a exportação sanitizada.
Não pretendo enviar a pasta privada `patches/`, nem testar os limites da
plataforma com arquivos criptografados. A própria documentação do Internet
Archive alerta que arquivos criptografados ou executáveis podem ser removidos,
e sua política prevê remoção por reclamação de copyright e encerramento de
contas reincidentes.

Antes da primeira publicação, ainda será necessário decidir:

- nome, licença e aviso legal do projeto;
- se os manifestos SC originais entram ou se publicamos apenas sua
  representação normalizada;
- quais campos dos registros de aquisição são estritamente necessários;
- como citar Sony, ProsperoPatches e outras fontes sem sugerir afiliação;
- periodicidade dos snapshots e política para correções;
- procedimento para pedidos legítimos de remoção.

## Fases

### 1. Auditoria local

Catalogar todos os formatos de sidecar existentes, identificar dados pessoais
ou desnecessários e definir um esquema estável para o registro público.

### 2. Exportador em modo de simulação

Criar uma ferramenta que apenas mostre o que seria publicado, acompanhada de
testes que comprovem a exclusão de `.pkg`, dumps, imagens e segredos.

### 3. Revisão manual

Gerar uma exportação de poucos títulos, revisar cada byte dos arquivos
resultantes e comparar o inventário público com a allowlist.

### 4. Repositório piloto

Publicar somente os registros de um pequeno conjunto já concluído. Observar se
o formato é compreensível, útil e sustentável antes de ampliar o escopo.

### 5. Snapshot arquivístico

Quando o repositório estiver estável, criar um snapshot no Internet Archive e
documentar exatamente o que foi enviado, seu hash e a relação com o commit de
origem.

## Critério de sucesso

O projeto será útil se uma terceira pessoa conseguir responder, usando apenas
o índice público:

- qual era a versão de um patch;
- quais peças oficiais o compunham;
- como ordená-las;
- qual deveria ser o tamanho e o hash do resultado;
- quando e como o conjunto foi verificado;
- se duas cópias representam exatamente o mesmo artefato.

Ele não precisa fornecer o conteúdo para preservar conhecimento verificável
sobre o conteúdo. Essa separação permite criar redundância pública agora,
enquanto mantenho os artefatos integrais sob uma política local mais cautelosa.

#ps5 #preservacao #patches #integridade #internet-archive #plano
