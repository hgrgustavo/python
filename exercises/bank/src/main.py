"""
Desafio
Aproveitando o algoritmo anterior, adicione:
   # Uma classe Cliente com os atributos:
        # nome
        # telefone.

   # Agora Modifique o metodo resumo da classe Conta para exibir:
        # o nome de cada cliente
        # telefone de cada cliente.

   # No final do programa crie dois objetos Cliente com seus argumentos

   Exemplo:
    maria = Cliente("Maria", "1243-3321")
    joão = Cliente("João", "5554-3322")
    conta = Conta([maria, joão], 1234, 5000)
    conta.resumo()

"""


class Client:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone


class Account:
    def __init__(self, clients: [], number: int, balance: float):
        self.clients = clients
        self.number = number
        self.balance = balance
        self.operations = []
        self.deposit(balance)

    def brief(self):
        print(f"CC N°{self.number}\n Saldo: {self.balance:10.2f}\n")

        for client in self.clients:
            print(f"Nome: {client.name}\n Telefone: {client.phone}")


    def withdraw(self, value: float):
        if self.balance >= value:
            self.balance -= value
            self.operations.append([f"SAQUE, R$ {value}"])

        else:
            print(f"SALDO INSUFICIENTE!, R${self.balance}")

    def deposit(self, value: float):
        self.balance += value
        self.operations.append([f"DEPÓSITO, R$ {value}"])


    def statement(self):
        print(f"EXTRATO CC N° {self.number}\n")

        for o in self.operations:
            print(f"{o[0]:10s}")
            print(f"\n SALDO: R${self.balance:10.2f}\n")
    

class SpecialAccount(Account):
    def __init__(self, clients: [], number: int, balance: float, limit: float):
        super().__init__(clients, number, balance)
        self.limit = limit
    
    def withdraw(self, value):
        if self.balance + self.limit >= value:
            self.balance -= value
            self.operations.append(["SAQUE", value])
        else:
            Account.withdraw(self, value)

        
        

maria = Client("Maria", "1243-3321")
joao = Client("João", "5554-3322")

conta = Account([maria, joao], 1234, 10000)
conta.statement()





