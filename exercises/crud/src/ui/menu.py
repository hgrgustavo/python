from tkinter import *
import subprocess


def abrir_login():
    caminho_py = r"C:\Users\SENAI\AppData\Local\Programs\Python\Python312\python.exe"
    caminho_arquivo = r"E:\python\exercises\crud\src\ui\login.py"
    subprocess.Popen([caminho_py, caminho_arquivo])


def abrir_cidade():
    caminho_py = r"C:\Users\SENAI\AppData\Local\Programs\Python\Python312\python.exe"
    caminho_arquivo = r"E:\python\exercises\crud\src\ui\city.py"
    subprocess.Popen([caminho_py, caminho_arquivo])


def abrir_usuario():
    caminho_py = r"C:\Users\SENAI\AppData\Local\Programs\Python\Python312\python.exe"
    caminho_arquivo = r"E:\python\exercises\crud\src\ui\user.py"
    subprocess.Popen([caminho_py, caminho_arquivo])


def abrir_cliente():
    caminho_py = r"C:\Users\SENAI\AppData\Local\Programs\Python\Python312\python.exe"
    caminho_arquivo = r"E:\python\exercises\crud\src\ui\client.py"
    subprocess.Popen([caminho_py, caminho_arquivo])


class Menu:
    def __init__(self, master):
        # title
        self.title_frame = Frame(master)
        self.title_label = Label(self.title_frame, text="MENU", font="Helvetica")

        self.title_frame.pack()
        self.title_label.pack()

        # buttons
        self.button_frame = Frame(master)

        self.user_button = Button(self.button_frame, background="blue", text="Usuário", font="Helvetica",
                                  foreground="white", width=25, command=abrir_usuario)

        self.button_frame.pack(pady=10)
        self.user_button.pack(pady=3)

        self.city_button = Button(self.button_frame, background="blue", text="Cidade", font="Helvetica",
                                  foreground="white", width=25,
                                  command=abrir_cidade)
        self.city_button.pack(pady=3)

        self.client_button = Button(self.button_frame, background="blue", text="Cliente", font="Helvetica",
                                    foreground="white", width=25,
                                    command=abrir_cliente)
        self.client_button.pack(pady=3)

        self.login_button = Button(self.button_frame, background="blue", text="Login", font="Helvetica",
                                   foreground="white", width=25, command=abrir_login)
        self.login_button.pack(pady=3)


window = Tk()
Menu(window)
window.geometry("600x400")
window.mainloop()
