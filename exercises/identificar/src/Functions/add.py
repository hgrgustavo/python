"""
Original function:

    def novo():
    global agenda, alterada
    nome = pede_nome()
    if pesquisa(nome) is not None:
        print("Nome já existe!")
        return
    telefone = pede_telefone()
    email = pede_email()
    aniversário = pede_aniversário()
    agenda.append([nome, telefone, email, aniversário])
    alterada = True
"""
from src.Functions.ask_name import ask_name
from src.Functions.ask_birthday import ask_birthday
from src.Functions.ask_email import ask_email
from src.Functions.ask_phone import ask_phone


def add():
    global agenda, alteration       # define scope

    name = ask_name()
    phone = ask_phone()
    email = ask_email()
    birthday = ask_birthday()

    agenda.append([name, phone, email, birthday])