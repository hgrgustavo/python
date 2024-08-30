from src.database.db import Database
from tkinter import messagebox



class Client:
    def __init__(self, client_id, name: str, cpf: str, phone: str, email: str, address: str):
        self.dict: {}
        self.id = client_id
        self.name = name
        self.cpf = cpf
        self.phone = phone
        self.email = email
        self.address = address

    def insert(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute(
                "insert into client (name, cpf, phone, email, address) values ('" + self.name + "', '" + self.cpf + "', '" + self.phone + "', '" + self.email + "', '" + self.address + "')")
            database.connection.commit()
            database.cursor.close()

            return messagebox.showinfo("", "Cliente cadastrado com sucesso.")

        except:
            return messagebox.showerror("", "Erro ao cadastrar cliente.")

    def update(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute(
                "update client set name = '" + self.name + "', cpf = '" + self.cpf + "', phone = '" + self.phone + "', email = '" + self.email + "' where id = '" + self.id + "'")
            database.connection.commit()

            return messagebox.showinfo("", "Cliente atualizado com sucesso.")

        except:
            return messagebox.showerror("", "Erro ao atualizar cliente.")

    def delete(self) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("delete from client where id = " + self.id + "")
            database.connection.commit()
            database.cursor.close()

            return messagebox.showinfo("", "Cliente excluido com sucesso.")

        except:
            return messagebox.showerror("", "Erro ao excluir cliente.")

    def select(self, client_id) -> messagebox:
        database = Database()

        try:
            database.cursor.execute("select * from client where id = " + client_id + "")

            data = []

            for row in data:
                self.id = row[0]
                self.name = row[1]
                self.cpf = row[2]
                self.phone = row[3]
                self.email = row[4]
                self.address = row[5]

            database.cursor.close()

            return messagebox.showinfo("", "Busca feita com sucesso.")

        except:
            return messagebox.showerror("", "Erro ao buscar cliente.")
