import os
os.system('cls || clear')


quantidade_num = 0 
soma_num = 0 # Valor das notas somadas


while True: # laço de repetição para validar as notas
    print(f'\nDigite o {quantidade_num + 1}ª número')
    num = int(input())
    if num >= 0:
        soma_num += num
        quantidade_num += 1
    else:
        media = soma_num / quantidade_num # Cálculo da média
        print(f'\nA média é {media:.2f}')
        print(f'Esse algoritimo teve {quantidade_num} números válidas')
        break
    
    
