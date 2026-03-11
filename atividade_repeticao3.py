import os
os.system('cls || clear')
import time

print('Digite 5 números inteiros (ex: 5, 4, 3 ,2 ,1):')
num1, num2 , num3, num4, num5 = map(int, input().split(', '))

soma = num1 + num2 + num3 + num4 + num5
print(f'A soma dos números é: {soma}')