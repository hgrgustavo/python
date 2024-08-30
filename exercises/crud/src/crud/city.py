from src.database.db import Database
from tkinter import messagebox



class City:
    def __init__(self, city_id, name: str, uf: str):
        self.dict: {}

        self.id = city_id
        self.name = name
        self.uf = uf

    def insert(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("insert into city (name, uf) values ('" + self.name + "', '" + self.uf + "'")
            database.connection.commit()
            database.cursor.close()

            return messagebox.showinfo("", "Cidade cadastrada com sucesso.")

        except:
            return messagebox.showerror("", "Erro ao cadastrar cidade.")

    def update(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("update city set name = '" + self.name + "', '" + self.uf + "'")
            database.connection.commit()
            database.cursor.close()

            return messagebox.showinfo("", "Cidade atualizada com sucesso.")

        except:
            return messagebox.showerror("", "Erro ao atualizar cidade.")

    def delete(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("delete from city where id = '" + self.id + "'")
            database.connection.commit()
            database.cursor.close()

            return messagebox.showinfo("", "Cidade excluida com sucesso.")

        except:
            return messagebox.showerror("", "Erro ao excluir cidade.")

    def select(self, city_id) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("select * from city where id = '" + city_id + "'")
            database.connection.commit()
            database.cursor.close()

            data = []

            for row in data:
                self.id = row[0]
                self.name = row[1]
                self.uf = row[2]

            return messagebox.showinfo("", "Busca feita com sucesso.")

        except:
            return messagebox.showerror("", "Erro ao buscar cidade.")
