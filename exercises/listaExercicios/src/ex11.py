# 11) Elaborar um programa Python para verificar se uma string é uma palindrome

palavra = input("Digite uma palavra: ")
inversa = palavra[::-1]
if palavra == inversa:
    print("É uma palíndrome")
else:
    print("Não é uma palíndrome")
    