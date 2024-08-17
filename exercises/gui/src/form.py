from tkinter import *


class Acesso:
    def __init__(self, master=None):
        self.fonte = "Arial, 10"

        self.container_1 = Frame(master)
        self.container_1["pady"] = 20
        self.container_1.pack()

        self.container_2 = Frame(master)
        self.container_2["padx"] = 20
        self.container_2.pack()

        self.container_3 = Frame(master)
        self.container_3["padx"] = 20
        self.container_3.pack()

        self.container_4 = Frame(master)
        self.container_4["padx"] = 20
        self.container_4.pack()

        self.titulo = Label(self.container_1, text="LOGIN")
        self.titulo["font"] = "arial", "15", "bold"
        self.titulo.pack()

        # name input
        self.label_nome = Label(self.container_2, text="NOME   ", font=self.fonte)
        self.label_nome.pack(side=LEFT)
        self.nome = Entry(self.container_2, width=30, font=self.fonte)
        self.nome.pack(side=LEFT)

        # password input
        self.label_senha = Label(self.container_3, text="SENHA  ", font=self.fonte)
        self.label_senha.pack(side=LEFT)
        self.senha = Entry(self.container_3, width=30, font=self.fonte, show="*")
        self.senha.pack(side=LEFT)

        # auth input
        self.auth = Button(self.container_4)
        self.auth["text"] = "AUTENTICAR"
        self.auth['font'] = self.fonte
        self.auth["width"] = 30
        self.auth["command"] = self.verificar_auth
        self.auth.pack()

        # msg pop-up
        self.msg = Label(self.container_4, text="", font=self.fonte)
        self.msg.pack()

        # verify auth
    def verificar_auth(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        if usuario == "Gus" and senha == "dev":
            self.msg["text"] = f"{usuario}, você foi autenticado. Bem-vindo!"

        else:
            self.msg["text"] = "NOME ou SENHA inválidos :("


root = Tk()
Acesso(root)
root.mainloop()

"nome:  "
"senha: "
