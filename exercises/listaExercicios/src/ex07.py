# 7) Elaborar um programa Python para calcular o fatorial de um número

num = int(input("Digite um número: "))

if num > -1:
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
        print("O fatorial de", num, " é ", fatorial)
else:
    print("Entrada inválida!")
