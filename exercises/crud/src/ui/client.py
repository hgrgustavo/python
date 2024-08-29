from tkinter import ttk

from src.crud.client import Client
from tkinter import *

from src.treeview import fetch_data, populate_treeview


class ClientApp:
    def __init__(self, master):
        # std font
        self.font = ("Helvetica", "8")

        # title
        self.title_frame = Frame(master)
        self.title_label = Label(self.title_frame, text="CADASTRO DE ", font=self.font)

        self.title_frame.pack()
        self.title_label.pack()

        # id
        self.id_frame = Frame(master)
        self.id_label = Label(self.id_frame, text="ID", font=self.font, width=5)
        self.id_entry = Entry(self.id_frame, width=5, font=self.font)

        self.id_frame.pack(pady=12)
        self.id_label.pack(side=LEFT)
        self.id_entry.pack(side=LEFT)

        # name
        self.name_frame = Frame(master)
        self.name_label = Label(self.name_frame, text="NOME", font=self.font, width=5)
        self.name_entry = Entry(self.name_frame, font=self.font)

        self.name_frame.pack(pady=6)
        self.name_label.pack(side=LEFT)
        self.name_entry.pack()

        # cpf
        self.cpf_frame = Frame(master)
        self.cpf_label = Label(self.cpf_frame, text="CPF", font=self.font, width=5)
        self.cpf_entry = Entry(self.cpf_frame, font=self.font)

        self.cpf_frame.pack(pady=6)
        self.cpf_label.pack(side=LEFT)
        self.cpf_entry.pack()

        # phone
        self.phone_frame = Frame(master)
        self.phone_label = Label(self.phone_frame, text="TELEFONE", font=self.font, width=5)
        self.phone_entry = Entry(self.phone_frame, font=self.font)

        self.phone_frame.pack(pady=6)
        self.phone_label.pack(side=LEFT)
        self.phone_entry.pack()

        # email
        self.email_frame = Frame(master)
        self.email_label = Label(self.email_frame, text="EMAIL", font=self.font, width=5)
        self.email_entry = Entry(self.email_frame, font=self.font)

        self.email_frame.pack(pady=6)
        self.email_label.pack(side=LEFT)
        self.email_entry.pack()

        # address
        self.address_frame = Frame(master)
        self.address_label = Label(self.address_frame, text="ENDEREÇO", font=self.font, width=10)
        self.address_entry = Entry(self.address_frame, font=self.font)

        self.address_frame.pack()
        self.address_label.pack(side=LEFT)
        self.address_entry.pack()

        # search button
        self.search_button = Button(self.id_frame, text="BUSCAR", font=self.font, width=10, command=self.select)
        self.search_button.pack(side=RIGHT, padx=5)

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

        # pop-up message
        self.message_frame = Frame(master)
        self.message_label = Label(self.message_frame, font=self.font)

        self.message_frame.pack()
        self.message_label.pack()

        # treeview area
        treeview_obj = ttk.Treeview(master, columns=("ID", "NOME", "CPF", "TELEFONE", "EMAIL", "ENDEREÇO"), show="headings")

        treeview_obj.heading("ID", text="ID")
        treeview_obj.heading("NOME", text="NOME")
        treeview_obj.heading("CPF", text="CPF")
        treeview_obj.heading("TELEFONE", text="TELEFONE")
        treeview_obj.heading("EMAIL", text="EMAIL")
        treeview_obj.heading("ENDEREÇO", text="ENDEREÇO")

        data = fetch_data("client")

        populate_treeview(treeview_obj, data)

        treeview_obj.pack(fill=BOTH, expand=True)

    # crud methods
    def insert(self):
        client = Client(self.id_entry.get(), self.name_entry.get(), self.cpf_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.address_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)

        self.message_label["text"] = client.insert()

    def update(self):
        client = Client(self.id_entry.get(), self.name_entry.get(), self.cpf_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.address_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)

        self.message_label["text"] = Client.update(client)

    def delete(self):
        client = Client(self.id_entry.get(), self.name_entry.get(), self.cpf_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.address_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)

        self.message_label["text"] = Client.delete(client, self.id_entry.get())

    def select(self):
        client = Client(self.id_entry.get(), self.name_entry.get(), self.cpf_entry.get(), self.phone_entry.get(), self.email_entry.get(), self.address_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.cpf_entry.delete(0, END)
        self.phone_entry.delete(0, END)
        self.email_entry.delete(0, END)
        self.address_entry.delete(0, END)

        self.message_label["text"] = Client.select(client, self.id_entry.get())


window = Tk()
ClientApp(window)
window.geometry("1350x650")
window.mainloop()
