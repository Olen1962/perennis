# 🌍 Perennis - Projeto Ecuménico

> **"A verdade é uma só. Os sábios chamam-na por nomes diferentes."**

## 📌 Sobre

Projeto dedicado à tradução, adaptação, comentário e análise comparativa de obras espíritas, ecuménicas e filosóficas (Allan Kardec, Francisco Cândido Xavier, Teosofia, Buda, Krishna, etc.), com foco na unidade da Verdade.

## 🗂 Estrutura do Projeto

```text
perennis/
├── autores/
│   ├── allan-kardec/{obras,traducoes,analises}/
│   ├── chico-xavier/{obras,traducoes,analises}/
│   ├── teosofia/{obras,traducoes,analises}/
│   ├── budismo/{obras,traducoes,analises}/
│   ├── hinduismo/{obras,traducoes,analises}/
│   └── outros/{obras,traducoes,analises}/
├── conceitos-comuns/
├── comparacoes/
├── traducoes/{em-andamento,finalizadas}/
├── modelos/
├── tags/README.md
├── content/
├── layouts/_default/
├── static/css/
├── config.toml
├── Makefile
├── GUIA-TRADUCOES.md
└── .gitignore
```

## 🚀 Como Usar

```bash
# Instalar Hugo no FreeBSD
sudo pkg install hugo

# Gerar o sítio
hugo --minify

# Iniciar servidor de desenvolvimento
hugo server -D --port 1313
```

Aceda a: http://localhost:1313

## 📝 Como Adicionar Conteúdo

1. Copie um modelo da pasta `modelos/`
2. Preencha os metadados
3. Adicione o conteúdo em Markdown
4. Teste com `hugo server -D`
