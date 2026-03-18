import os
os.system('cls || clear')
import time

QUANTIDADE_NOTAS = 2 # Quantidade de notas q vão ser utilizadas
soma_notas = 0 # Valor das notas somadas
for i in range(QUANTIDADE_NOTAS): # Quantidade de notas a serem digitadas
    while True: # laço de repetição para validar as notas
        print(f'\nDigite a {i + 1}ª nota')
        notas = float(input())
        if notas >= 0 and notas <= 10: # if else para validar as notas
            soma_notas += notas
            break
        else:
            print('Essa nota não existe')
            
media = soma_notas / QUANTIDADE_NOTAS # Cálculo da média
print(f'\nA média é {media:.2f}')