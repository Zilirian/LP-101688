import os
os.system('cls || clear')

import os
os.system('cls || clear')

vetor_num = []
soma_num_positivo = 0
num_negativo = 0

for i in range(5):
    num = float(input('Digite um número: '))
    vetor_num.append(num)

print()    
for negativo in vetor_num:
    if negativo < 0:
        negativo = 0
    print(negativo)


print('\n' * 3)
