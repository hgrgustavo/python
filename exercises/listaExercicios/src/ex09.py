# 9) Elaborar um programa Python para imprimir a tabuada de um número

continua = True

while continua:
    n = int(input("Digite um número: "))
    for i in range(1, 11):
        print(n, "x", " = ", n * 1)
    resposta = input("Deseja continuar (s / n)?")
    if resposta == "n":
        continua = False
        