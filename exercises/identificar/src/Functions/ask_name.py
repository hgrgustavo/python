"""
Original Function:

    def pede_nome(padrão=""):
        nome = input("Nome: ")
        if nome == "":
            nome = padrão
        return nome

"""

def ask_name(std = ""):
    name: str = input("Name: ")

    if name == "":
        name = std

    return name