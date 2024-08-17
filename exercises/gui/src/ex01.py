"""
Exercício 1 - Posicionamento de Labels
"""

from tkinter import *


class Ex01:
    def __init__(self, master):
        self.container = Frame(master)
        self.container.pack()

        self.label_up = Label(self.container, text="TOP")
        self.label_up.pack(side=TOP)

        self.label_bottom = Label(self.container, text="BOTTOM")
        self.label_bottom.pack(side=BOTTOM)

        self.label_left = Label(self.container, text="LEFT")
        self.label_left.pack(side=LEFT)

        self.label_right = Label(self.container, text="     RIGHT")
        self.label_right.pack(side=RIGHT)


root = Tk()
Ex01(root)
root.mainloop()
