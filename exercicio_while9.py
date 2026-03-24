import os
os.system('cls || clear')


quantidade_num = 0 
soma_num = 0 # Valor das notas somadas
quantidade_num_par = 0
quantidade_num_impar = 0
soma_num_par = 0
soma_num_impar = 0

while True: # laço de repetição para validar as notas
    print(f'\nDigite o {quantidade_num + 1}ª número')
    num = int(input())
    soma_num += num
    quantidade_num += 1
    if num % 2 == 0:
        quantidade_num_par += 1  
        soma_num_par += num
    else:
        quantidade_num_impar += 1  
        soma_num_impar += num
    if num == 0:
        media = soma_num / quantidade_num # Cálculo da média
        media_par = soma_num_par / quantidade_num_par 
        
        print(f'\nA quantidade de números pares é {quantidade_num_par} e ímpares é {quantidade_num_impar}')
        print(f'A média é {media:.2f}')
        print(f'A média dos números pares é {media_par:.2f}')
        print(f'Esse algoritimo teve {quantidade_num} números válidas')
        break
    