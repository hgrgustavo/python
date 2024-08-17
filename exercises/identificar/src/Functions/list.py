"""
Oringinal function:

    def lista():
    print("\nAgenda\n\n------")
    # Usamos a função enumerate para obter a posição na agenda
    for posição, e in enumerate(agenda):
        # Imprimimos a posição
        print(f"\nPosição: {posição}")
        mostra_dados(e[0], e[1], e[2], e[3])
    print("------\n")
"""
from src.Functions.show_data import show_data


def list():
    print("\n Agenda \n\n ---------")

    for position, e in enumerate(agenda):
        print(f"\n Position? {position}")

        show_data(e[0], e[1], e[2], e[3])

    print("--------------")