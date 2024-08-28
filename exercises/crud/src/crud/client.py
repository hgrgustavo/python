from src.database.db import Database

database = Database()


class Client:
    def __init__(self, client_id, name: str, cpf: str, phone: str, email: str, address: str):
        self.dict: {}
        self.id = client_id
        self.name = name
        self.cpf = cpf
        self.phone = phone
        self.email = email
        self.address = address

    def insert(self) -> str:
        try:
            database.cursor.execute(
                "insert into Client (name, cpf, phone, email, address) values ('" + self.name + "', '" + self.cpf + "', '" + self.phone + "', '" + self.email + "', '" + self.address + "')")
            database.commit()
            database.cursor.close()

            return "Cliente cadastrado com sucesso"

        except:
            return "Ocorreu um erro no cadastro de cliente"

    def update(self):
        try:
            database.cursor.execute(
                "update client set name = '" + self.name + "', cpf = '" + self.cpf + "', phone = '" + self.phone + "', email = '" + self.email + "' where id = '" + self.id + "'")
            database.connection.commit()

            return "Cliente atualizado!"

        except:
            return "erro na atualização do cliente!"

    def delete(self, client_id):
        try:
            database.cursor.execute("delete from cliente where id = " + client_id + "")
            database.connection.commit()
            database.cursor.close()

            return "Cliente excluído com sucesso!"

        except:
            return "Erro na exclusão do cliente"

    def select(self, client_id):
        try:
            database.cursor.execute("select * from cliente where id = " + client_id + "")

            data = []

            for row in data:
                self.id = row[0]
                self.name = row[1]
                self.cpf = row[2]
                self.phone = row[3]
                self.email = row[4]
                self.address = row[5]

            database.cursor.close()

            return "Busca feita com sucesso!"

        except:
            return "Ocorreu um erro na busca do usuário"
