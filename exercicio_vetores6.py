import os
os.system('cls || clear')

vetor_num = []
soma_num_positivo = 0
num_negativo = 0

for i in range(5):
    num = float(input('Digite um número: '))
    vetor_num.append(num)
    
for negativo in vetor_num:
    if negativo < 0:
        num_negativo +=1
for positivo in vetor_num:
    if positivo >= 0:
        soma_num_positivo += positivo
print(f'\nA quantidade de números negativos é {num_negativo}')
print(f'e a soma de números positivos é {soma_num_positivo}')
print('\n' * 3)
