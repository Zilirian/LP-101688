import os
os.system('cls || clear')

num = []

for i in range(6):
    print(f'Digite o {i + 1}º número: ')
    num.append(int(input()))
    
    # código q informa quantos são pares e quanto sãos ímpares
pares = 0
ímpares = 0
for um_num in num:
    if um_num % 2 == 0:
        pares += 1
    else:
        ímpares += 1
print(f'\nQuantidade de números pares: {pares}')
print(f'Quantidade de números ímpares: {ímpares}')