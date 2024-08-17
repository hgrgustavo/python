# https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html#install-in-tool-window
# https://www.tcl.tk/about/uses.html
# https://github.com/python/cpython/tree/d7a3df91505faa56c51d169648253bd0d57ddae2/Lib/tkinter
# https://docs.python.org/3.11/library/tkinter.html#tkinter.Tk





class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        
        # pack is a geometry manager. Scripts that controls the GUI widgets positioning, behavior, ...
        self.widget1.pack()

        self.msg = Label(self.widget1, text="Primeiro widget(container)")
        self.msg["font"] = "Verdana", 10, "italic", "bold"
        self.msg.pack()

        self.sair = Button(self.widget1)

        self.sair["text"] = "Clique aqui"
        self.sair["font"] = "Calibri", '10'
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack()

    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"


root = Tk()
Application(root)
root.mainloop()
