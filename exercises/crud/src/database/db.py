"""
Criar uma nova tabela no banco
    - cidades
    - clientes

Altere a aplicação
    - Botão usuário (login)
    - Botão cidades (cidae estado, pais)
    - Botão clientes (nome, cpf, email)

"""
import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect("sqlite3.db")
        self.cursor = self.connection.cursor()

        self.create_table_user()
        self.create_table_city()
        self.create_table_client()

    def create_table_user(self):
        self.cursor.execute("""
                    create table if not exists user (
                        id integer primary key autoincrement,
                        name text,
                        phone integer,
                        email text,
                        username text,
                        password text    
                    )
        """)

    def create_table_city(self):
        self.cursor.execute("""
                    create table if not exists city (
                        id integer primary key autoincrement,
                        name text,
                        uf text
                    )
        """)

    def create_table_client(self):
        self.cursor.execute("""
                    create table if not exists client (
                        id integer primary key autoincrement,
                        name text,
                        cpf text,
                        phone text,
                        email text,
                        address text
                        
                    )
        """)

    def commit(self):
        self.connection.commit()
        self.cursor.close()
