"""
Elaborar um programa Python para:

- Receber uma lista de inteiros
- Separar os números positivos (n > -1) dos negativos (n < 0)

"""


def find_positive(listnum: int) -> int:
    return listnum > -1


def find_negative(listnum: int) -> int:
    return listnum < 0


mylist = []

for i in range(1, 3):
    input_value = int(input("Digite um valor positivo ou negativo: "))
    mylist.append(input_value)

print("\nLista: ", mylist)
print("Positivos: ", filter(find_positive, mylist).__str__())
print("Negativos: ", filter(find_negative, mylist).__str__())
