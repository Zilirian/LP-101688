import os
os.system("cls || clear")
import time

print('Diga um número:')
num = int(input())

for i in range(num, 0, -1):
    print(i)
    time.sleep(1)
    