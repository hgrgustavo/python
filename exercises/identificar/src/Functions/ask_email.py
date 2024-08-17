"""
Original function:

    def pede_email(padrão=""):
    email = input("Email: ")
    if email == "":
        email = padrão
    return email

"""

def ask_email(std = ""):
    email = input("E-mail: ")

    if email == "":
        email = std

    return email
