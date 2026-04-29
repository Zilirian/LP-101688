import os
from dataclasses import dataclass

os.system('cls')

#Definindo uma classe
@dataclass
class Endereco:
    logradouro: str
    numero: str

#Definindo uma classe
@dataclass
class Cliente:
    nome: str
    idade: int
    endereco: Endereco

    def mostrar_dados(self):
        print(f'''
Nome: {self.nome}
Idade: {self.idade}
Endereço: {self.endereco.logradouro}
Número: {self.endereco.numero}
              ''')
        
print('= Solicitando dados do cliente =')
cliente = Cliente(
        nome= input('Digite seu nome: '),
        idade= int(input('Digite sua idade: '))
        
)