import os
os.system('cls || clear')


quantidade_notas = 0 
soma_notas = 0 # Valor das notas somadas


while True: # laço de repetição para validar as notas
    print(f'\nDigite a {quantidade_notas + 1}ª nota')
    notas = float(input())
    if notas >= 0 and notas <= 10: # if else para validar as notas
        soma_notas += notas
        quantidade_notas += 1
        print('Você deseja digitar mais notas? (s/n)')	
        resposta = input().lower()
        if resposta == 'n':
            break
    else:
        print('Essa nota não existe')
            
media = soma_notas / quantidade_notas # Cálculo da média
print(f'\nA média é {media:.2f}')