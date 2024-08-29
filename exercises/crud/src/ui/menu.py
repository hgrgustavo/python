from tkinter import *
import subprocess


def open_file_login():
    exe_path = r"C:\Users\SENAI\AppData\Local\Programs\Python\Python312\python.exe"
    file_path = r"E:\python\exercises\crud\src\ui\login.py"
    subprocess.Popen([exe_path, file_path])


def open_file_city():
    exe_path = r"C:\Users\SENAI\AppData\Local\Programs\Python\Python312\python.exe"
    file_path = r"E:\python\exercises\crud\src\ui\city.py"
    subprocess.Popen([exe_path, file_path])


def open_file_user():
    exe_path = r"C:\Users\SENAI\AppData\Local\Programs\Python\Python312\python.exe"
    file_path = r"E:\python\exercises\crud\src\ui\user.py"
    subprocess.Popen([exe_path, file_path])


def open_file_client():
    exe_path = r"C:\Users\SENAI\AppData\Local\Programs\Python\Python312\python.exe"
    file_path = r"E:\python\exercises\crud\src\ui\client.py"
    subprocess.Popen([exe_path, file_path])


class Menu:
    def __init__(self, master):
        # title
        self.title_frame = Frame(master)
        self.title_label = Label(self.title_frame, text="MENU", font="Helvetica")

        self.title_frame.pack()
        self.title_label.pack()

        # buttons
        self.button_frame = Frame(master)
        self.user_button = Button(self.button_frame, background="blue", text="Usuário", font="Helvetica", foreground="white", width=25, command=open_file_user)

        self.button_frame.pack(pady=10)
        self.user_button.pack(pady=3)

        self.city_button = Button(self.button_frame, background="blue", text="Cidade", font="Helvetica", foreground="white", width=25, command=open_file_city)
        self.city_button.pack(pady=3)

        self.client_button = Button(self.button_frame, background="blue", text="Cliente", font="Helvetica", foreground="white", width=25, command=open_file_client)
        self.client_button.pack(pady=3)

        self.login_button = Button(self.button_frame, background="blue", text="Login", font="Helvetica", foreground="white", width=25, command=open_file_login)
        self.login_button.pack(pady=3)


window = Tk()
Menu(window)
window.geometry("600x400")
window.mainloop()
