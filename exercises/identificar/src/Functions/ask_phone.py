"""
Original function:

    def pede_telefone(padrão=""):
    telefone = input("Telefone: ")
    if telefone == "":
        telefone = padrão
    return telefone

"""

def ask_phone(std = ""):
    phone: str = input("Phone: ")

    if phone == "":
        phone = std

    return phone
