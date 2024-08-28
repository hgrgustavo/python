"""
1° Impressão do estoque atual
2° Faz a venda, imprimindo-a
3° Melhorar os outputs
4° Impressão do estoque atualizado

"""

estoque = {
    "tomate": [1000, 2.30], 
    "alface": [500, 0.45], 
    "batata": [2001, 1.20], 
    "feijão": [100, 1.50], 
}

print(":::::::::: Estoque atual :::::::::::")
for chave, dados in estoque.items():
    print("NOME DO PRODUTO: ", chave)
    print("QUANTIDADE: ", dados[0])
    print(f"PREÇO: {dados[1]:6.2f}\n")

total = 0

print(":::::: CADASTRO DE VENDAS :::::::\n")

while True:
    print("ENTRE x PARA SAIR\n")
    produto: str = input("NOME DO PRODUTO: ")

    if produto == "x" or "X":
        break

    if produto in estoque:
        quantidade = int(input(f"QUANTIDADE DE " + produto + ": "))
        
        if quantidade <= estoque[produto][0]:
            preco = estoque[produto][1]
            custo = preco * quantidade
            print(f"{produto:12s}: {quantidade:3d} x {preco:6.2f} = {custo:6.2f}")
            estoque[produto][0] -= quantidade
            total += custo

            print("::::: VENDA REALIZADA! :::::::")
            print("NOME DO PRODUTO: ", produto)
            print("QUANTIDADE: ", quantidade)
            print(f"PREÇO: R$ ", preco)

            print(f" CUSTO: R$ {total:21.2f}\n")

        else:
            print("QUANTIDADE INSUFICIENTE")


print(":::::: ESTOQUE ATUALIZADO :::::::\n")
for chave, dados in estoque.items():
    print("NOME DO PRODUTO: ", chave)
    print("QUANTIDADE: ", dados[0])
    print(f"PREÇO: R$ {dados[1]:6.2f}\n")
