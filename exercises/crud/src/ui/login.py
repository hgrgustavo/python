import tkinter.font
from tkinter import *

std_font = tkinter.font.Font


class Login:
    def __init__(self, master):
        # title
        self.title_frame = Frame(master)
        self.title_label = Label(self.title_frame, text="LOGIN", font="Helevetica")

        self.title_frame.pack()
        self.title_label.pack()

        # username
        self.username_frame = Frame(master)
        self.username_label = Label(self.username_frame, text="Username: ")
        self.username_entry = Entry(self.username_frame)

        self.username_frame.pack()
        self.username_label.pack(side=LEFT)
        self.username_entry.pack()

        # password
        self.password_frame = Frame(master)
        self.password_label = Label(self.password_frame, text="Password: ")
        self.password_entry = Entry(self.password_frame)

        self.password_frame.pack()
        self.password_label.pack(side=LEFT, padx=1.4)
        self.password_entry.pack()

        # button
        self.button_frame = Frame(master)
        self.button_font = tkinter.font.Font(family="Helvetica", size=6)
        self.button = Button(self.button_frame, background="blue", text="Entrar", font=self.button_font,
                             foreground="white", width=25)

        self.button_frame.pack()
        self.button.pack()


root = Tk()
Login(root)
root.mainloop()
