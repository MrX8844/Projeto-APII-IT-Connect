import sqlite3

def criar_tabelas():
    con = sqlite3.connect("suporte_tecnico.db")
    cursor = con.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS chamadas (
                id INTEGER PRIMARY KEY,
                nome_solicitante TEXT,
                departamento TEXT,
                equipamento TEXT,
                descricao_problema TEXT,
                prioridade TEXT,
                status TEXT,
                data_abertura DATE NOT NULL
                );
                """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS tecnicos (
                id INTEGER PRIMARY KEY,
                nome_tecnico TEXT,
                email TEXT UNIQUE NOT NULL,
                senha TEXT NOT NULL,
                especialidade TEXT,
                disponibilidade TEXT
                );
                """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS historico_login (
                id INTEGER PRIMARY KEY,
                nome_tecnico TEXT,
                email TEXT NOT NULL,
                data_login DATE
                );
                """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS historico_chamadas (
                id INTEGER PRIMARY KEY,
                nome_solicitante TEXT,
                departamento TEXT,
                nome_tecnico TEXT,
                especialidade_tecnico TEXT,
                descricao_problema TEXT,
                status TEXT,
                data_abertura DATE NOT NULL
                );
                """)
    con.commit()
    con.close()

criar_tabelas()