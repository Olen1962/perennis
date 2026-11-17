.PHONY: ajuda construir servir novo limpar

ajuda:
	@echo "Projeto Perennis - Comandos Hugo"
	@echo "  make construir   - Gerar sítio"
	@echo "  make servir      - Iniciar servidor (http://localhost:1313)"
	@echo "  make novo        - Criar novo ficheiro"
	@echo "  make limpar      - Limpar ficheiros gerados"

construir:
	hugo --minify --cleanDestinationDir

servir:
	hugo server -D --port 1313

novo:
	@echo "Uso: make novo SECCAO=autores/allan-kardec/traducoes FICHEIRO=novo-ficheiro"
	@hugo new ${SECCAO}/${FICHEIRO}.md

limpar:
	rm -rf public/ resources/_gen/

