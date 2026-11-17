# CHECKLIST.md

Lista de acompanhamento do desenvolvimento e manutenção do projeto Perennis.

## 1. Preparação e estrutura

- [x] Criar a estrutura inicial do projeto Hugo.
- [x] Organizar os conteúdos por autores e áreas temáticas.
- [x] Criar as secções de análises, obras e traduções.
- [x] Criar as secções de comparações e conceitos comuns.
- [x] Criar as áreas de traduções em andamento e finalizadas.
- [x] Criar os modelos de conteúdo em `modelos/`.
- [x] Criar os layouts principais em `layouts/_default/`.
- [x] Configurar o menu principal.
- [x] Configurar as taxonomias do Hugo.
- [x] Criar o `Makefile` com os comandos principais.
- [x] Criar o `README.md`.
- [x] Criar o presente ficheiro de acompanhamento.

## 2. Configuração do Hugo

- [x] Definir o endereço principal do projeto.
- [x] Configurar o idioma português (`pt-PT`).
- [x] Configurar a linguagem predefinida do conteúdo.
- [x] Configurar os metadados gerais do sítio.
- [x] Configurar os formatos de saída HTML e RSS.
- [x] Configurar as taxonomias `tags`, `autores` e `obras`.
- [x] Manter `unsafe = false` no processador Goldmark.
- [x] Criar o CSS personalizado em `static/css/custom.css`.
- [x] Confirmar a construção do sítio sem erros nem avisos relacionados com HTML.

## 3. Layouts e apresentação

- [x] Criar `layouts/_default/baseof.html`.
- [x] Criar `layouts/_default/list.html`.
- [x] Criar `layouts/_default/single.html`.
- [x] Criar a folha de estilos personalizada.
- [x] Separar o HTML dos conteúdos Markdown quando necessário.
- [x] Criar um shortcode para o formulário de inscrição.
- [ ] Rever a apresentação visual em diferentes resoluções.
- [ ] Verificar a navegação entre todas as secções.
- [ ] Rever a apresentação das páginas de autores, obras e traduções.

## 4. Página de inscrição

- [x] Criar `content/inscricao.md`.
- [x] Definir os metadados da página.
- [x] Preparar o texto de apresentação da inscrição.
- [x] Criar `layouts/shortcodes/formulario-inscricao.html`.
- [x] Integrar o shortcode na página de inscrição.
- [x] Manter o HTML do formulário fora do Markdown.
- [x] Confirmar a construção sem avisos de HTML omitido.
- [ ] Definir o mecanismo de receção das inscrições.
- [ ] Implementar o envio dos dados do formulário.
- [ ] Implementar validação e tratamento de erros.
- [ ] Testar o processo completo de inscrição.
- [ ] Definir a política de privacidade e o tratamento dos dados pessoais.

## 5. Produção de conteúdos

### 5.1. Tipos de conteúdo

- [ ] Conteúdos originais.
- [ ] Traduções.
- [ ] Adaptações.
- [ ] Comentários.
- [ ] Análises.
- [ ] Comparações.
- [ ] Investigações críticas.
- [ ] Reflexões próprias.
- [ ] Sínteses.

### 5.2. Organização

- [ ] Confirmar a localização adequada de cada novo conteúdo.
- [ ] Associar os conteúdos aos respetivos autores e obras.
- [ ] Utilizar os modelos disponíveis em `modelos/`.
- [ ] Preencher corretamente os metadados.
- [ ] Utilizar as taxonomias de forma consistente.
- [ ] Verificar as ligações entre conteúdos relacionados.

### 5.3. Revisão editorial

- [ ] Verificar a fidelidade às fontes.
- [ ] Distinguir claramente fontes, interpretações e conclusões próprias.
- [ ] Identificar a autoria e a origem das citações.
- [ ] Indicar as edições e versões utilizadas.
- [ ] Assinalar dúvidas e ambiguidades.
- [ ] Evitar apresentar interpretações como factos documentados.
- [ ] Rever a terminologia e a coerência conceptual.
- [ ] Rever a ortografia e a gramática em português europeu.

## 6. Traduções

- [ ] Seguir as orientações de `GUIA-TRADUCOES.md`.
- [ ] Identificar a obra e a versão original.
- [ ] Registar as referências bibliográficas.
- [ ] Manter a fidelidade ao sentido do texto original.
- [ ] Assinalar expressões ambíguas ou de difícil tradução.
- [ ] Distinguir tradu