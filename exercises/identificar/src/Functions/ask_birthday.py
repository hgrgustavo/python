"""
Original function:

    def pede_aniversário(padrão=""):
    aniversário = input("Data de aniversário: ")
    if aniversário == "":
        aniversário = padrão
    return aniversário

"""

def ask_birthday(std = ""):
    birthday: str = input("Birthday: ")

    if birthday == "":
        birthday = std

    return birthday
