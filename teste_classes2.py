from os import system as sy
from dataclasses import dataclass
sy('cls')

@dataclass          #chama a funçao que constroi classes de forma simplificada
class Pessoa:
    nome: str      # declara o tipo do atributo
    idade: int     # declara o tipo do atributo

@dataclass       
class Cachorro:       
    nome: str      
    idade: int     
                   
                   

n_cachorros = []
n_pessoas = []
def exibir_dados():
    for i, p in enumerate(n_pessoas):
        print(f'{p.nome} tem um cachorro chamado {n_cachorros[i].nome}.')
    
pessoa1 = Pessoa('maria', 18)
pessoa2 = Pessoa('bob', 30)
cachorro1 = Cachorro('alex', 4)
cachorro2 = Cachorro('bolt',3)

n_pessoas.append(pessoa1)
n_pessoas.append(pessoa2)
n_cachorros.append(cachorro1)
n_cachorros.append(cachorro2)

exibir_dados()
cachorro1.exibir_dados()  # Exemplo de chamada do método
cachorro2.exibir_dados()