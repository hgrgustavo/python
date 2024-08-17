class Pessoa:

    # Construtor especial
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # metodo saudação
    def saudacao(self):
        return f"Seu nome é: {self.nome} e sua idade é {self.idade} anos"

# criando objeto 'obj' da classe Pessoa
obj = Pessoa("Jão", 789)

print(obj.nome)
print(obj.idade)

print(obj.saudacao())