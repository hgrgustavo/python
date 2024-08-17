"""
Desafio
Aproveitando o algoritmo anterior, adicione:
   # Uma classe Cliente com os atributos:
        # nome
        # telefone.

   # Agora Modifique o método resumo da classe Conta para exibir:
        # o nome de cada cliente
        # telefone de cada cliente.

   # No final do programa crie dois objetos Cliente com seus argumentos

   Exemplo:
    maria = Cliente("Maria", "1243-3321")
    joão = Cliente("João", "5554-3322")
    conta = Conta([maria, joão], 1234, 5000)
    conta.resumo()

"""


class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone


class Conta:
    def __init__(self, clientes, numero, saldo=0):

        self.saldo = 0
        self.clientes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)

    def resumo(self):
        print(f"CC N°{self.numero}\n Saldo: {self.saldo:10.2f}\n Nome: {self.nome}\n Telefone: {self.telefone}")

        for cliente in self.clientes:
            print(f"Nome: {cliente.nome}\n Telefone: {cliente.telefone}")

    def saque(self, valor):

        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente!")

    def deposito(self, valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])

    def extrato(self):
        print(f"Extrato CC N° {self.numero}\n")
        for o in self.operacoes:
            print(f"{o[0]:10s} {o[1]:10.2f}")
            print(f"\n Saldo: {self.saldo:10.2f}\n")


class ContaEspecial(Conta):
    def __init__(self, clientes, numero, saldo=0, limite=0):
        Conta.__init__(self, clientes, numero)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            Conta.saque(self, valor)


maria = Cliente("Maria", "1243-3321")
joão = Cliente("João", "5554-3322")

conta = Conta([maria, joão], 1234)
conta.resumo()
