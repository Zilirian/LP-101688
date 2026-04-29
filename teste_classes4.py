from os import system as sy
from dataclasses import dataclass

def limpar_tela():
    sy('cls')

@dataclass
class Funcionario:
    nome: str
    matricula: int
    e_mail: str
    setor: str

    def __str__(self):
        return f'{self.nome} ({self.matricula}) - {self.setor} - {self.e_mail}'

def criar_funcionario():
    nome = input('Digite seu nome: ')
    while True:
        try:
            matricula = int(input('Digite sua matricula: '))
            break
        except ValueError:
            print('Digite um valor válido')
            limpar_tela()

    e_mail = input('Digite seu e_mail: ')
    setor = input('Digite seu setor: ')
    return Funcionario(nome, matricula, e_mail, setor)

def main():
    limpar_tela()
    funcionarios = []
    funcionarios.append(criar_funcionario())
    funcionarios.append(criar_funcionario())
    
    for func in funcionarios:
        print(func)

if __name__ == '__main__':
    main()
