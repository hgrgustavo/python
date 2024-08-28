"""
Escreva um programa Python que:
 1° Gere um dicionário em que:
    # Cada chave seja um caractere,
    # Seu valor seja o número da posição desse caractere encontrado em uma frase lida.
    # Exemplo: O rato → { “O”:1, “r”:2, “a”:3, “t”:4, “o”:5}

"""


# Exemplo do Gemini!
def criar_dicionario_posicoes(frase: str):
    dicionario_posicoes = {}
    
    for indice, caractere in enumerate(frase):
        if caractere not in dicionario_posicoes:
            dicionario_posicoes[caractere.strip()] = indice + 1  # +1 para começar a contagem em 1
            
        if caractere == " ":
            indice += 1
    return dicionario_posicoes


# Exemplo de uso:
frase = input("Digite uma frase: ")
resultado = criar_dicionario_posicoes(frase)
print(resultado)
