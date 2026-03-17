import os
os.system("cls || clear")
import time

print('Diga um número:')
num = int(input())

for i in range(10):
    multiplicacao = num * i
    print(f'\n{num} * {i} = {multiplicacao}')
    time.sleep(1)