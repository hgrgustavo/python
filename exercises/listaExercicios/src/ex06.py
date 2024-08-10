# 6) Elaborar um programa Python para calcular as raízes da equação do segundo grau

import math
import cmath

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

if a == 0:
    print("Não é uma equação do segundo grau!!!")

else:
    delta = math.pow(b, 2) - 4 * a * c

    if delta < 0:
        x1 = (-b + cmath.sqrt(delta)) / (2 * a)
        x2 = (-b - cmath.sqrt(delta)) / (2 * a)

        print("Raízes complexas: ", x1, " e ", x2)

    elif delta == 0:
        x = -b / (2 * a)

        print("Uma raíz real: ", x)

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)

        print("Duas raízes reais: ", x1, " e ", x2)



