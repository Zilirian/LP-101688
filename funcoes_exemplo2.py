from os import system
system('cls')

def saudacao(nome):
    print(f'Olá, {nome}, seja bem vindo!')

nome1 = input('Digite seu nome: ')
saudacao(nome1)