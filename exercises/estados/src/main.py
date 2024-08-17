"""
Crie classes para representar estados e cidades.
Cada estado tem um nome, sigla e cidades.
Cada cidade tem nome e população.

Escreva um programa de testes que crie três estados com algumas cidades em cada um.
Exiba a população de cada estado
Exiba a soma da população de suas cidades.

"""


class Estado:
    def _init_(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def adiciona_cidade(self, cidade):
        cidade.estado = self
        self.cidades.append(cidade)

    def somarpop(self):
        return sum([c.populacao for c in self.cidades])


class Cidade:
    def _init_(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
        self.estado = None


am = Estado("Amazonas", "AM")

am.adiciona_cidade(Cidade("Manaus", 1861838))
am.adiciona_cidade(Cidade("Parintins", 103828))
am.adiciona_cidade(Cidade("Itacoatiara", 89064))

sp = Estado("São Paulo", "SP")

sp.adiciona_cidade(Cidade("São Paulo", 11376685))
sp.adiciona_cidade(Cidade("Guarulhos", 1244518))
sp.adiciona_cidade(Cidade("Campinas", 1098630))

# cmd /c mklink . 'C:\Users\SENAI\Documents\ALUNO\Nova pasta\xampp\MercuryMail\sqlite3.exe'  creates a symlink
