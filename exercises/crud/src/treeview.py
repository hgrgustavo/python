

# Função para popular a Treeview com os dados do banco
def populate_treeview(treeview, data):
    for row in data:
        treeview.insert("", "end", values=row)


# treeview events
def select_event_city(self, event):
    if self.treeview_obj.selection():
        item = self.treeview_obj.selection()
        value: [] = self.treeview_obj.item(item, "values")

        self.id.delete(0, END)
        self.name.delete(0, END)
        self.state.delete(0, END)

        self.id.insert(INSERT, value[0])
        self.name.insert(INSERT, value[1])
        self.state.insert(INSERT, value[2])

        """
            bind event
            
            self.treeview_obj.bind("<<TreeviewSelect>>", self.select_city_event)
        """

def select_event_user(self, event):
    if self.treeview_obj.selection():
        item = self.treeview_obj.selection()
        value: [] = self.treeview_obj.item(item, "values")

        self.id.delete(0, END)
        self.name.delete(0, END)
        self.phone.delete(0, END)
        self.email.delete(0, END)
        self.username.delete(0, END)
        self.password.delete(0, END)

        self.id.insert(INSERT, value[0])
        self.name.insert(INSERT, value[1])
        self.phone.insert(INSERT, value[2])
        self.email.insert(INSERT, value[3])
        self.username.insert(INSERT, value[4])
        self.password.insert(INSERT, value[5])

        """
            bind event
            
            self.treeview_obj.bind("<<TreeviewSelect>>", self.select_user_event)
        """

def select_event_client(self, event):
    if treeview_obj.selection():
        item = treeview_obj.selection()
        value: [] = treeview_obj.item(item, "values")

        self.id.delete(0, END)
        self.name.delete(0, END)
        self.cpf.delete(0, END)
        self.phone.delete(0, END)
        self.email.delete(0, END)
        self.address.delete(0, END)

        self.id.insert(INSERT, value[0])
        self.name.insert(INSERT, value[1])
        self.cpf.insert(INSERT, value[2])
        self.phone.insert(INSERT, value[3])
        self.email.insert(INSERT, value[4])
        self.address.insert(INSERT, value[5])

        """
            bind event
            
            self.treeview_obj.bind("<<TreeviewSelect>>", select_event_client)
        
        """

"""
# Configurando a interface principal

root = tk.Tk()
root.title("Exibindo Dados do Banco de Dados")

# Configurando a Treeview
columns = ("ID", "Nome", "Telefone", "Email")  # Definindo as colunas
treeview = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    treeview.heading(col, text=col)

treeview.pack(fill=tk.BOTH, expand=True)

# Pegando os dados do banco e populando a Treeview

data = fetch_data()
populate_treeview(treeview, data)

# Iniciando a aplicação
root.mainloop()
"""