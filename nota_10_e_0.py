import os
os.system('cls || clear')

print('Digite uma nota entre 0 e 10')
nota = int(input())

if nota >= 0 and nota <= 10:
    print('O número está entre 0 e 10')
else:
    print('O número deve estar entre 0 e 10')
