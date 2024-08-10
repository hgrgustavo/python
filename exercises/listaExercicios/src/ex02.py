# 2) Elaborar um programa Python para somar os digitos de um número menor que 100.

num = int(input("Digite um número menor que 100: "))

if num > 99:
    print("Número inválido :(")
else:
    print("Soma: ", num // 10 + num % 10)