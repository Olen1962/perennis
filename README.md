# Perennis

> **A verdade é uma só. Os sábios chamam-na por nomes diferentes.**

## Sobre

O Perennis é, прежде de tudo, um **acervo multidisciplinar** de obras espíritas, religiosas, filosóficas e de outras áreas do conhecimento. Reúne fontes documentais de diferentes autores e tradições, procurando consolidar pontes de união e atenuar divisões entre diferentes formas de pensamento.

Entre as fontes de estudo encontram-se Allan Kardec, Francisco Cândido Xavier, André Luiz, a Teosofia, o Budismo e o Hinduísmo.

## Princípio de organização editorial

O acervo documental tem autonomia relativamente aos estudos e às opiniões que possam nascer da sua leitura. A fonte não deve ser confundida com a interpretação.

O Perennis distingue três espaços editoriais:

1. **Acervo** — obras, documentos, fontes, edições, traduções e adaptações, organizados por autores, tradições e áreas do conhecimento.
2. **Estudos** — análises, ensaios, investigações, comparações e estudos temáticos, sempre relacionados com as fontes utilizadas.
3. **Pensamento** — reflexões pessoais, opiniões, hipóteses, dúvidas e questões em aberto, com possibilidade de acompanhar a evolução das ideias e preservar versões anteriores.

Os três espaços podem estabelecer ligações e referências cruzadas, mas não devem ser fundidos. Uma opinião não é um documento-fonte; uma hipótese não é um facto estabelecido; uma análise não substitui a obra analisada.

A expressão que resume este princípio é: **não confundir a estrada da beira com a beira da estrada.**

## Estrutura editorial prevista

A organização de conteúdos a implementar em `content/` deverá refletir esta separação:

```text
content/
├── acervo/
│   ├── autores/
│   │   ├── allan-kardec/
│   │   ├── chico-xavier/
│   │   ├── budismo/
│   │   ├── hinduismo/
│   │   ├── teosofia/
│   │   └── outros/
│   └── areas/
├── estudos/
│   ├── analises/
│   ├── comparacoes/
│   └── temas/
├── pensamento/
│   ├── reflexoes/
│   ├── hipoteses/
│   └── questoes/
└── inscricao.md
```

Esta é a organização de referência; a migração da estrutura atual será feita de forma gradual, preservando os conteúdos, as ligações e os endereços sempre que possível. A organização interna de cada autor será definida de acordo com a natureza das obras e dos documentos. Não se deve presumir que todas as tradições utilizem a mesma estrutura editorial.

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
