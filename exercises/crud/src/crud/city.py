from src.database.db import Database

database = Database()

class City:
    def __init__(self, cidade_id, nome: str, uf:str):
        self.dict: {}

        self.id = cidade_id
        self.nome = nome
        self.uf = uf

    def insert(self) -> str:
        try:
            database.cursor.execute("insert into cidade (nome, uf) values ('" + self.nome + "', '" + self.uf + "'")
            database.commit()
            database.cursor.close()

            return "Cidade cadastrada com sucesso!"

        except:
            return "Erro ao cadastrar cidade!"

    def update(self) -> str:
        try:
            database.cursor.execute("update cidade set nome = '" + self.nome + "', '" + self.uf + "'")
            database.commit()
            database.cursor.close()

            return "Cidade atualizada com sucesso!"

        except:
            return "Erro ao atualizar cidade!"

    def delete(self) -> str:
        try:
            database.cursor.execute("delete from cidade where id = '" + self.id + "'")
            database.commit()
            database.cursor.close()

            return "Cidade excluida com sucesso!"
        except:
            return "Erro ao excluir cidade!"

    def select(self, cidade_id) -> str:
        try:
            database.cursor.execute("select * from cidade where id = '" + cidade_id +"'")
            database.commit()
            database.cursor.close()

            data = []

            for row in data:
                self.id = row[0]
                self.nome = row[1]
                self.uf = row[2]

            return "Busca feita com sucesso!"

        except:
            return "Erro ao buscar cidade!"





