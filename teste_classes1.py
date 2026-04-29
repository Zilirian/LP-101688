from os import system as sy
sy('cls')

class Pessoa:
    def __init__(self, nm='', idd = 0):
        self.nome = nm
        self.idade = idd

    def exibir_dados(self):
        print(f'{self.nome} tem {self.idade} anos de idade.')

pessoa1 = Pessoa('maria', 18)
pessoa2 = Pessoa('bob', 30)

pessoa1.exibir_dados()
pessoa2.exibir_dados()