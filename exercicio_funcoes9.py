from os import system
from datetime import date
from time import sleep

import os
os.system('cls || clear')
 
def transformacao(peso, altura):
    return peso / (altura ** 2) 

def classificacao(imc):
        if imc >= 40:
            return 'Obesidade Grau III (Mórbida)'
        elif imc >= 35 and imc <= 39.9:
            return 'Obesidade Grau II (Severa)'
        elif imc >= 30 and imc <= 34.9:
            return 'Obesidade Grau I'
        elif imc >= 25 and imc <= 29.9:
            return 'Sobrepeso'
        elif imc >= 18.5 and imc <= 24.9:
            return 'Peso ideal'
        elif imc >= 17 and imc <= 18.4:
            return 'Abaixo do Peso'

def main():
    
    while True:
        try:
            peso_pessoa = float(input('Digite seu peso: '))
            altura_pessoa = float(input('Digite sua altura: '))
            total = transformacao(peso_pessoa, altura_pessoa)
        except ValueError:
            system('cls')
            print( 'Digite valores válidos')
        classe = classificacao(imc=total)
        print(f'\nSeu IMC é: {total:.2f} e sua classificação é: {classe}.')
        print('Operação finalizada')
        print('\n' * 4)

main()