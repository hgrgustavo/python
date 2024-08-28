from src.database.db import Database

database = Database()


class User:
    def __init__(self, user_id, name: str, phone: str, email: str, username: str, password: str):
        self.dict: {}

        self.id = user_id
        self.name = name
        self.phone = phone
        self.email = email
        self.username = username
        self.password = password

    def insert(self):
        try:
            database.cursor.execute(
                "insert into usuario (name, phone, email, username, password) values ('" + self.name + "', '" + self.phone + "', '" + self.email + "', '" + self.username + "', '" + self.password + "')")
            database.commit()
            database.cursor.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Erro ao cadastrar usuário!"

    def update(self):
        try:
            database.cursor.execute(
                "update usuario set name = '" + self.name + "', '" + self.phone + "', '" + self.email + "', '" + self.username + "', '" + self.password + "'")
            database.commit()
            database.cursor.close()

            return "Usuário atualizado com sucesso!"

        except:
            return "Erro ao atualizar usuário"

    def delete(self, user_id):
        try:
            database.cursor.execute("delete from usuario where id = '" + user_id + "'")
            database.commit()
            database.cursor.close()

            return "Usuário excluido com sucesso!"

        except:
            return "Erro ao excluir usuário"

    def select(self, user_id):
        try:
            database.cursor.execute("select * from usuario where id = '" + user_id + "'")
            database.commit()
            database.cursor.close()

            data = []

            for row in data:
                self.id = row[0]
                self.name = row[1]
                self.phone = row[2]
                self.email = row[3]
                self.username = row[4]
                self.password = row[5]

            return "Busca feita com sucesso!"

        except:
            return "Erro ao buscar usuário!"
