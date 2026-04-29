from os import system as sy
from dataclasses import dataclass
sy('cls')

@dataclass
class Funcionario:
    nome: str
    matricula: int
    e_mail: str
    setor: str

    def exibir_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Matricula: {self.matricula}')
        print(f'E_mail: {self.e_mail}')
        print(f'Setor: {self.setor}')

funcionario1 = Funcionario('silas', 1234567, 'silas@gmail.com', "Administração")
funcionario1.exibir_dados()



