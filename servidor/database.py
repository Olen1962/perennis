
import sqlite3
from contextlib import closing
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = DATA_DIR / "inscricoes.db"


def ligar():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    db = sqlite3.connect(DB_PATH, timeout=10)
    db.row_factory = sqlite3.Row

    return db


def inicializar():
    with closing(ligar()) as db:
        with db:
            db.execute("""
                CREATE TABLE IF NOT EXISTS inscricoes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    data_inscricao TEXT NOT NULL DEFAULT
                        (datetime('now', 'localtime')),
                    estado TEXT NOT NULL DEFAULT 'pendente'
                )
            """)

            db.execute("""
                CREATE UNIQUE INDEX IF NOT EXISTS
                    idx_inscricoes_email_unico
                ON inscricoes(email COLLATE NOCASE)
            """)


def guardar_inscricao(nome, email):
    with closing(ligar()) as db:
        with db:
            cursor = db.execute("""
                INSERT INTO inscricoes (nome, email)
                VALUES (?, ?)
            """, (nome, email))

            return cursor.lastrowid
