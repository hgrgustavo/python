"""
Original function:
    def apaga():
    global agenda, alterada
    nome = pede_nome()
    p = pesquisa(nome)

    if p is not None:
        if confirma("apagamento") == "S":
            del agenda[p]
            alterada = True
    else:
        print("Nome não encontrado.")
"""
from src.Functions.ask_name import ask_name
from src.Functions.confirm import confirm
from src.Functions.find import find


def delete():
    global agenda, alteration

    name = ask_name()
    f = find(name)

    if f is not None and confirm("delete") == "Y":
        del agenda[f]
        alteration = True
    else:
        print(f"Cannot find {name}")
