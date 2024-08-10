# 10) Elaborar um programa Python para ler 10 números e imprimir a soma, o maior e o menor
# desses números.

array = []
for i in range(10):
    num = int(input("Digite um número: "))
    array.append(num)

soma = sum(array)
maior = max(array)
menor = min(array)

print("Soma: ")
print("Maior: ")
print("Menor: ")

    