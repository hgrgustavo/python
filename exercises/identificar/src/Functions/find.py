"""
Original function:

    def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:
            return p
    return None

"""

def find(name: str):
    lowercase_name = name.lower()
    for p, e in enumerate(agenda):      # Agenda should be global
        if e[0].lower() == lowercase_name:
            return p
    return None
