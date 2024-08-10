# 3) Elaborar um programa Python para calcular a área de um triângulo.

base = float(input("Digite a base do triângulo: "))
height = float(input("Digite a altura do triângulo: "))
const = 0.5

area = (base * height) * const

print("Área: ", round(area, 2))

