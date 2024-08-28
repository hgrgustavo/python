"""
connect to crud
"""

from tkinter import *
from src.crud.user import User


class UserApp:
    def __init__(self, master=None):
        # std font
        self.font = ("Helvetica", "8")

        # title
        self.title_frame = Frame(master, pady=10)
        self.title_label = Label(self.title_frame, text="Informe os dados", font=self.font)

        self.title_frame.pack()
        self.title_label.pack()

        # id
        self.id_frame = Frame(master, padx=20, pady=5)
        self.id_label = Label(self.id_frame, text="ID", font=self.font, width=5)
        self.id_entry = Entry(self.id_frame, width=5, font=self.font)

        self.id_frame.pack()
        self.id_label.pack(side=LEFT)
        self.id_entry.pack(side=LEFT)

        # name
        self.name_frame = Frame(master, padx=20, pady=5)
        self.name_label = Label(self.name_frame, text="NOME", font=self.font, width=10)
        self.name_entry = Entry(self.name_frame, width=25, font=self.font)

        self.name_frame.pack()
        self.name_label.pack(side=LEFT)
        self.name_entry.pack(side=LEFT)

        # phone
        self.phone_frame = Frame(master, padx=20, pady=5)
        self.phone_label = Label(self.phone_frame, text="TELEFONE", font=self.font, width=10)
        self.phone_entry = Entry(self.phone_frame, width=25, font=self.font)

        self.phone_frame.pack()
        self.phone_label.pack(side=LEFT)
        self.phone_entry.pack(side=LEFT)

        # email
        self.email_frame = Frame(master, padx=20, pady=5)
        self.email_label = Label(self.email_frame, text="EMAIL", font=self.font, width=10)
        self.email_entry = Entry(self.email_frame, width=25, font=self.font)

        self.email_frame.pack()
        self.email_label.pack(side=LEFT)
        self.email_entry.pack(side=LEFT)

        # username
        self.username_frame = Frame(master, padx=20, pady=5)
        self.username_label = Label(self.username_frame, text="USERNAME", font=self.font, width=10)
        self.username_entry = Entry(self.username_frame, width=25, font=self.font)

        self.username_frame.pack()
        self.username_label.pack(side=LEFT)
        self.username_entry.pack(side=LEFT)

        # senha
        self.password_frame = Frame(master, padx=20, pady=5)
        self.password_label = Label(self.password_frame, text="SENHA", font=self.font, width=10)
        self.password_entry = Entry(self.password_frame, width=25, show="•", font=self.font)

        self.password_frame.pack()
        self.password_label.pack(side=LEFT)
        self.password_entry.pack(side=LEFT)

        # search button
        self.search_button = Button(self.id_frame, text="BUSCAR", font=self.font, width=10, command=self.select)
        self.search_button.pack(side=RIGHT, padx=15)

        self.buttons_frame = Frame(master)
        self.buttons_frame.pack()

        # insert button
        self.insert_button = Button(self.buttons_frame, text="INSERIR", font=self.font, width=10, command=self.insert)
        self.insert_button.pack(side=RIGHT)

        # update button
        self.update_button = Button(self.buttons_frame, text="ATUALIZAR", font=self.font, width=10, command=self.update)
        self.update_button.pack(side=RIGHT)

        # delete button
        self.delete_button = Button(self.buttons_frame, text="DELETAR", font=self.font, width=10, command=self.delete)
        self.delete_button.pack(side=RIGHT)

        # pop-up message
        self.message_frame = Frame(master)
        self.message_label = Label(self.message_frame, text="", font=self.font)

        self.message_frame.pack()
        self.message_label.pack()

    # crud methods
    def insert(self):
        user = User(self.id_entry.get(), self.name_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.username_entry.get(), self.password_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        self.message_label["text"] = user.insert()

    def update(self):
        user = User(self.id_entry.get(), self.name_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.username_entry.get(), self.password_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        self.message_label["text"] = user.update()

    def delete(self):
        user = User(self.id_entry.get(), self.name_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.username_entry.get(), self.password_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        self.message_label["text"] = User.delete(user, self.id_entry.get())

    def select(self):
        user = User(self.id_entry.get(), self.name_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.username_entry.get(), self.password_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)

        self.message_label["text"] = User.select(user, self.id_entry.get())


window = Tk()
UserApp(window)
window.geometry("600x400")
window.mainloop()
