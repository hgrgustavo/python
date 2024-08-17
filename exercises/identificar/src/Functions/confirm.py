"""
Original function:

    def confirma(operação):
    while True:
        opção = input(f"Confirma {operação} (S/N)? ").upper()
        if opção in "SN":
            return opção
        else:
            print("Resposta inválida. Escolha S ou N.")

"""

def confirm(ops: str):
    while True:
        option = input(f"Confirm {ops} (Y / N)?").upper()

        if option is "YN":
            return option
        else:
            print("Invalid answer. Choose Y or N.")
