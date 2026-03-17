import os
os.system('cls || clear')
import time
import math
pares = 0
impares = 0
numeros = []
for i in range(5):
    num = int(input('Digite um número inteiro:'))
    numeros.append(num)
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1 
total = sum(numeros)


print(f'\nÍmpares:{impares}')
print(f'\npares:{pares}')