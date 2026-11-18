# CHECKLIST.md

Lista de acompanhamento do desenvolvimento e manutenção do projeto Perennis. As tarefas só são assinaladas como concluídas depois de confirmadas no repositório ou testadas.

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
- [x] Configurar `defaultContentLanguage = "pt"`.
- [x] Configurar os metadados gerais do sítio.
- [x] Configurar os formatos de saída HTML e RSS.
- [x] Configurar as taxonomias `tags`, `autores` e `obras`.
- [x] Manter `unsafe = false` no processador Goldmark.
- [x] Criar o CSS personalizado em `static/css/custom.css`.
- [x] Confirmar a construção do sítio sem erros nem avisos relacionados com HTML.
- [x] Não definir `languageCode = "pt-PT"`, opção que originou aviso de depreciação.

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

### 5.1. Modelos editoriais

- [x] Criar `modelo-analise.md`.
- [x] Criar `modelo-traducao.md`.
- [x] Criar `modelo-original-pt-br.md` para preservar obras originais brasileiras.
- [x] Criar `modelo-adaptacao-pt-pt.md` para adaptações editoriais para português europeu.
- [ ] Rever e uniformizar os metadados dos modelos.
- [ ] Criar modelos específicos adicionais apenas quando a necessidade estiver identificada.

### 5.2. Organização dos conteúdos

- [ ] Confirmar a localização adequada de cada novo conteúdo.
- [ ] Associar os conteúdos aos respetivos autores e obras.
- [ ] Utilizar o modelo adequado em `modelos/`.
- [ ] Preencher corretamente os metadados.
- [ ] Utilizar as taxonomias de forma consistente.
- [ ] Verificar as ligações entre conteúdos relacionados.
- [ ] Implementar a organização de Allan Kardec por língua: original francês e traduzido português.
- [ ] Implementar a distinção entre originais pt-BR e adaptações pt-PT para Chico Xavier.
- [ ] Preparar a página da série «A Vida no Mundo Espiritual», de André Luiz.
- [ ] Registar os 13 volumes da série e iniciar o trabalho por «Nosso Lar».
- [ ] Tratar os prefácios e textos associados como documentos identificados e ligados às respetivas obras.

### 5.3. Revisão editorial

- [ ] Verificar a fidelidade às fontes.
- [ ] Distinguir claramente fontes, interpretações e conclusões próprias.
- [ ] Identificar a autoria e a origem das citações.
- [ ] Indicar as edições e versões utilizadas.
- [ ] Assinalar dúvidas e ambiguidades.
- [ ] Evitar apresentar interpretações como factos documentados.
- [ ] Rever a terminologia e a coerência conceptual.
- [ ] Rever a ortografia e a gramática em português europeu.

## 6. Traduções e adaptações

- [ ] Seguir as orientações de `GUIA-TRADUCOES.md`.
- [ ] Identificar a obra e a versão original.
- [ ] Registar as referências bibliográficas.
- [ ] Manter a fidelidade ao sentido do texto original.
- [ ] Assinalar expressões ambíguas ou de difícil tradução.
- [ ] Distinguir traduções de adaptações editoriais.
- [ ] Manter os originais disponíveis para comparação.
- [ ] Rever e comparar cada tradução ou adaptação com a fonte.
- [ ] Atualizar os metadados e o estado de cada trabalho.

## 7. Testes e construção

- [ ] Confirmar os comandos `make construir`, `make servir` e `make limpar`.
- [ ] Executar uma construção completa com `make construir`.
- [ ] Confirmar que a construção termina sem erros.
- [ ] Testar localmente todas as páginas.
- [ ] Verificar ligações internas e externas.
- [ ] Verificar imagens e outros recursos.
- [ ] Verificar os ficheiros RSS e sitemap.
- [ ] Rever os metadados e a apresentação nos motores de pesquisa.

## 8. Publicação

- [ ] Confirmar o estado do repositório Git.
- [ ] Rever as alterações antes de cada commit.
- [ ] Confirmar que os ficheiros gerados não são adicionados indevidamente.
- [ ] Construir novamente o sítio antes da publicação.
- [ ] Publicar as alterações no repositório remoto.
- [ ] Confirmar a atualização do sítio publicado.
- [ ] Verificar o funcionamento do domínio perennis.pt.

## 9. Manutenção

- [ ] Manter este checklist atualizado.
- [ ] Atualizar README.md quando houver alterações relevantes.
- [ ] Manter a documentação coerente com a estrutura real do projeto.
- [ ] Rever periodicamente os modelos de conteúdo.
- [ ] Rever as configurações e dependências do Hugo.
- [ ] Eliminar apenas ficheiros gerados que possam ser recriados.
- [ ] Não alterar a estrutura das secções sem necessidade justificada.
