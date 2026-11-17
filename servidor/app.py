
import os
import re
import sqlite3
import time

from flask import Flask, jsonify, request

from database import inicializar, guardar_inscricao


app = Flask(__name__)

app.config["MAX_CONTENT_LENGTH"] = 16 * 1024

ORIGENS_PERMITIDAS = {
    origem.strip()
    for origem in os.environ.get(
        "PERENNIS_ALLOWED_ORIGINS",
        "http://localhost:1313,http://127.0.0.1:1313"
    ).split(",")
    if origem.strip()
}


@app.after_request
def configurar_cors(resposta):
    origem = request.headers.get("Origin")

    if origem in ORIGENS_PERMITIDAS:
        resposta.headers["Access-Control-Allow-Origin"] = origem
        resposta.headers["Vary"] = "Origin"
        resposta.headers["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        resposta.headers["Access-Control-Allow-Headers"] = "Content-Type"

    return resposta



@app.route("/api/inscricoes", methods=["POST", "OPTIONS"])
def inscricoes():
    if request.method == "OPTIONS":
        return "", 204

    if not request.is_json:
        return jsonify({
            "erro": "Formato de dados inválido."
        }), 415

    dados = request.get_json(silent=True)

    if not isinstance(dados, dict):
        return jsonify({
            "erro": "Dados inválidos."
        }), 400

    nome = dados.get("nome")
    email = dados.get("email")

    # Proteção anti-spam: honeypot
    website = dados.get("website", "")

    if not isinstance(website, str) or website.strip():
        return jsonify({
            "erro": "Não foi possível validar a submissão."
        }), 400

    # Proteção anti-spam: tempo mínimo de preenchimento
    form_started_at = dados.get("form_started_at")

    try:
        inicio = int(form_started_at)
    except (TypeError, ValueError):
        return jsonify({
            "erro": "Não foi possível validar a submissão."
        }), 400

    tempo_decorrido = time.time() - inicio

    if tempo_decorrido < 3:
        return jsonify({
            "erro": "A submissão foi efetuada demasiado depressa."
        }), 400

    if not isinstance(nome, str) or not isinstance(email, str):
        return jsonify({
            "erro": "Nome e correio eletrónico são obrigatórios."
        }), 400

    nome = nome.strip()
    email = email.strip().lower()

    if not nome or len(nome) > 150:
        return jsonify({
            "erro": "Indica um nome válido (máximo 150 caracteres)."
        }), 400

    if len(email) > 254 or not re.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+", email
    ):
        return jsonify({
            "erro": "Indica um endereço de correio eletrónico válido."
        }), 400

    try:
        identificador = guardar_inscricao(nome, email)

        return jsonify({
            "mensagem": "Inscrição recebida com sucesso.",
            "id": identificador
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({
            "erro": "Este endereço de correio eletrónico já tem uma inscrição."
        }), 409

    except Exception:
        app.logger.exception("Erro ao guardar inscrição")

        return jsonify({
            "erro": "Não foi possível guardar a inscrição."
        }), 500


inicializar()


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
