import os
os.system("cls || clear")
import time

numeros = []

for i in range(5):
    num = int(input('Digite um número inteiro:'))
    numeros.append(num)

total = sum(numeros)

print(f'Soma:{total}')

# ---- outra forma de resolver ----

# soma = 0
# for i in range(5):
#     numero = int(input('Digite um número:'))
#     soma = soma + numero or soma += numero
# print(f'A soma é {soma}')