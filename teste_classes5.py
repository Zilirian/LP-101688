from os import system as sy
from dataclasses import dataclass

def limpar_tela():
    sy('cls')

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float

    def __str__(self):
        return f'{self.nome} ({self.idade}) - {self.peso} - {self.altura}'

def criar_paciente():
    nome = input('Digite seu nome: ')
    while True:
        try:
            idade = int(input('Digite sua idade: '))
            break
        except ValueError:
            print('Digite um valor válido')
            limpar_tela()
    while True:
        try:
            peso = float(input('Digite seu peso: '))
            break
        except ValueError:
            print('Digite um valor válido')
            limpar_tela()
    while True:
        try:
            altura = float(input('Digite sua altura '))
            break
        except ValueError:
            print('Digite um valor válido')
            limpar_tela()
    
    return Paciente(nome, idade, peso, altura)

def main():
    limpar_tela()
    pacientes = []
    pacientes.append(criar_paciente())
    pacientes.append(criar_paciente())
    
    for pac in pacientes:
        print(pac)

if __name__ == '__main__':
    main()
