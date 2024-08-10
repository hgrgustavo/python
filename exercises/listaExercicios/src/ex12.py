# 12) Elaborar um programa Python para intercalar duas listas ordenadas

# list 1
lista1 = list()
i = 1
while i < 11:
    elem = int(input("Digite um elemento da lista: "))
    lista1.append(elem)
    i += 1

print(lista1)
lista1ordenada = sorted(lista1)
print(lista1ordenada)

# list 2
lista2 = list()
i = 1
while i < 11:
    elem = int(input("Digite um elemento da lista: "))
    lista2.append(elem)
    i += 1

print(lista2)
lista2ordenada = sorted(lista2)
print(lista2ordenada)

# processing
intercalada = []
i = j = 0

while i < len(lista1ordenada) and j < len(lista2ordenada):
    if lista1ordenada[i] < lista2ordenada[j]:
        intercalada.append(lista1ordenada[i])
        i += 1
    else:
        intercalada.append(lista2ordenada[j])
        j += 1

intercalada += lista1ordenada[i:]
intercalada += lista2ordenada[j:]

# final result
print(intercalada)