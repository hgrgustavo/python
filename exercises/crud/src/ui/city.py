"""
connect to database
add combo box
"""

from tkinter import *
from tkinter import ttk

from src.crud.city import City
from src.treeview import fetch_data, populate_treeview


class CityApp:
    def __init__(self, master):
        # std font
        self.font = ("Helvetica", "8")

        # title
        self.title_frame = Frame(master, pady=10)
        self.title_label = Label(self.title_frame, text="CADASTRO DE CIDADE", font=self.font)

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
        self.name_frame = Frame(master)
        self.name_label = Label(self.name_frame, text="NOME", font=self.font, width=5)
        self.name_entry = Entry(self.name_frame, font=self.font)

        self.name_frame.pack(pady=6)
        self.name_label.pack(side=LEFT)
        self.name_entry.pack()

        # state
        self.state_frame = Frame(master)
        self.state_label = Label(self.state_frame, text="UF", font=self.font, width=5)
        self.state_entry = Entry(self.state_frame, font=self.font)

        self.state_frame.pack(pady=6)
        self.state_label.pack(side=LEFT)
        self.state_entry.pack()

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

        # treeview area
        treeview_obj = ttk.Treeview(master, columns=("ID", "NOME", "ESTADO"), show="headings")

        treeview_obj.heading("ID", text="ID")
        treeview_obj.heading("NOME", text="NOME")
        treeview_obj.heading("ESTADO", text="ESTADO")

        data = fetch_data("city")

        populate_treeview(treeview_obj, data)

        treeview_obj.pack(fill=BOTH, expand=True)

    # crud methods
    def insert(self):
        city = City(self.id_entry.get(), self.name_entry.get(), self.state_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.state_entry.delete(0, END)

        self.message_label["text"] = city.insert()

    def delete(self):
        city = City(self.id_entry.get(), self.name_entry.get(), self.state_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.state_entry.delete(0, END)

        self.message_label["text"] = city.delete()

    def update(self):
        city = City(self.id_entry.get(), self.name_entry.get(), self.state_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.state_entry.delete(0, END)

        self.message_label["text"] = city.delete()

    def select(self):
        city = City(self.id_entry.get(), self.name_entry.get(), self.state_entry.get())

        self.id_entry.delete(0, END)
        self.name_entry.delete(0, END)
        self.state_entry.delete(0, END)

        self.message_label["text"] = city.select(self.id_entry.get())


window = Tk()
CityApp(window)
window.geometry("600x400")
window.mainloop()
