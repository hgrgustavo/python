"""
Elaborar um programa Python para:

- Somar todos os números pares entre 50 e 100
- Utilizar funções
- Imprimir a soma

"""


def pair_sum(start: int, finish: int) -> int:
    global totalSum
    for i in range(start, finish):
        if totalSum % 2 == 0:
            totalSum += totalSum

    return totalSum


print(pair_sum(50, 101))