"""
Escreva um programa que:
 1° Gere um dicionário em que:
    # Cada chave seja um caractere,
    # Seu valor seja o número da posição desse caractere encontrado em uma frase lida.
    # Exemplo: O rato → { “O”:1, “r”:2, “a”:3, “t”:4, “o”:5}

"""


dictionary: dict = {}
string: str = input("STRING: ")

for i in range(0, string.__len__()):
    if string.strip(" "):
        for char_key, char_value in dictionary.items():

            char_value[i] = i


print(dictionary.items())
