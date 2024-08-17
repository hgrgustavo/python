"""
Exercício 2 - Soma de inteiros

"""

from tkinter import *


class Ex02:
    def __init__(self, root):
        self.root_container = Frame(root)
        self.root_container.pack()

        # Entries
        self.entry_1 = Entry(self.root_container)
        self.entry_1.insert(0, "VALOR")
        self.entry_1.pack()

        self.entry_2 = Entry(self.root_container)
        self.entry_2.insert(1, "VALOR")
        self.entry_2.pack()


obj = Tk()
Ex02(obj)
obj.mainloop()
