import os
os.system('cls || clear')
import time

print('Digite um número:')
num = int(input())

print('\nContagem regresiva:')
for i in range(num, 0, -1):
    print(i)
    time.sleep(0.000000000000000000000000000000000000000000000005)