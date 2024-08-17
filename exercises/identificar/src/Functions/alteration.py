"""
Original function:

    def altera():
    global alterada
    p = pesquisa(pede_nome())
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        email = agenda[p][2]
        aniversário = agenda[p][3]
        print("Encontrado:")
        mostra_dados(nome, telefone, email, aniversário)
        nome = pede_nome(nome)  # Se nada for digitado, mantém o valor
        telefone = pede_telefone(telefone)
        email = pede_email(email)
        aniversário = pede_aniversário(aniversário)
        if confirma("alteração") == "S":
            agenda[p] = [nome, telefone, email, aniversário]
            alterada = True
    else:
        print("Nome não encontrado.")
"""
from src.Functions.ask_birthday import ask_birthday
from src.Functions.ask_email import ask_email
from src.Functions.ask_name import ask_name
from src.Functions.ask_phone import ask_phone
from src.Functions.find import find
from src.Functions.show_data import show_data


def alteration():
    global alt

    f = find(ask_name())

    if f is not None:
        name = agenda[f][0]         # define scope
        phone = agenda[f][1]
        email = agenda[f][2]
        birthday = agenda[f][3]

        print("Target found! Showing results...")
        show_data(name, phone, email, birthday)

        name = ask_name(name)
        phone = ask_phone(phone)
        email = ask_email(email)
        birthday = ask_birthday(birthday)
    else:
        print("Target not found :(")


