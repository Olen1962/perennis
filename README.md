# Perennis

> **A verdade é uma só. Os sábios chamam-na por nomes diferentes.**

## Sobre

O Perennis é um projeto de investigação, tradução, adaptação, comentário e análise de obras espíritas, religiosas e filosóficas, procurando consolidar pontes de união e atenuar divisões entre diferentes tradições de pensamento.

Entre as fontes de estudo encontram-se Allan Kardec, Francisco Cândido Xavier, André Luiz, a Teosofia, o Budismo e o Hinduísmo.

## Organização dos conteúdos

Os conteúdos do sítio encontram-se em `content/`, organizados por autores e áreas temáticas:

```text
content/
├── autores/
│   ├── allan-kardec/
│   ├── chico-xavier/
│   ├── budismo/
│   ├── hinduismo/
│   ├── teosofia/
│   └── outros/
├── comparacoes/
├── conceitos-comuns/
├── traducoes/
└── inscricao.md
```

A organização interna de cada autor será definida de acordo com a natureza das obras e dos documentos. Não se deve presumir que todas as tradições utilizem a mesma estrutura editorial.

### Obras de Chico Xavier

É necessário distinguir claramente:

- **Original em pt-BR:** texto da edição brasileira, preservado como fonte.
- **Adaptação em pt-PT:** versão editorial em português europeu, relacionada com o original e comparável com ele.

A adaptação não substitui o original. As opções editoriais e as diferenças relevantes devem ficar documentadas.

### Obras de Allan Kardec

A organização prevista distingue os textos em francês dos textos traduzidos para português:

- `original-frances/`
- `traduzido-portugues/`

A edição utilizada deve ser sempre identificada. Prefácios e outros documentos associados às obras são tratados como documentos integrantes do respetivo contexto editorial.

## Modelos editoriais

Os modelos encontram-se em `modelos/`:

| Modelo | Utilização |
|---|---|
| `modelo-original-pt-br.md` | Registo de uma obra original em português do Brasil |
| `modelo-adaptacao-pt-pt.md` | Adaptação editorial de pt-BR para pt-PT |
| `modelo-traducao.md` | Tradução |
| `modelo-analise.md` | Análise |

Ao criar um conteúdo, copiar o modelo adequado, preencher os metadados e identificar as fontes. Sempre que possível, indicar edição, capítulo, secção e página ou parágrafo.

## Desenvolvimento local

Requisitos: Hugo instalado.

```sh
# Construir o sítio
hugo --minify

# Iniciar o servidor de desenvolvimento
hugo server -D --port 1313
```

Aceder a http://localhost:1313.

No FreeBSD, Hugo pode ser instalado com:

```sh
sudo pkg install hugo
```

## Documentação de trabalho

- `CHECKLIST.md`: acompanhamento das tarefas.
- `GUIA-TRADUCOES.md`: orientações para traduções.
- `modelos/`: modelos de conteúdos editoriais.
