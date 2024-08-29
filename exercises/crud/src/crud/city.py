from src.database.db import Database

database = Database()

class City:
    def __init__(self, city_id, name: str, uf:str):
        self.dict: {}

        self.id = city_id
        self.name = name
        self.uf = uf

    def insert(self) -> str:
        try:
            database.cursor.execute("insert into city (name, uf) values ('" + self.name + "', '" + self.uf + "'")
            database.commit()
            database.cursor.close()

            return "Cidade cadastrada com sucesso!"

        except:
            return "Erro ao cadastrar cidade!"

    def update(self) -> str:
        try:
            database.cursor.execute("update city set name = '" + self.name + "', '" + self.uf + "'")
            database.commit()
            database.cursor.close()

            return "Cidade atualizada com sucesso!"

        except:
            return "Erro ao atualizar cidade!"

    def delete(self) -> str:
        try:
            database.cursor.execute("delete from city where id = '" + self.id + "'")
            database.commit()
            database.cursor.close()

            return "Cidade excluida com sucesso!"
        except:
            return "Erro ao excluir cidade!"

    def select(self, city_id) -> str:
        try:
            database.cursor.execute("select * from city where id = '" + city_id +"'")
            database.commit()
            database.cursor.close()

            data = []

            for row in data:
                self.id = row[0]
                self.name = row[1]
                self.uf = row[2]

            return "Busca feita com sucesso!"

        except:
            return "Erro ao buscar cidade!"





