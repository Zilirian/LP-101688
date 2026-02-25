import os
os.system('cls || clear')
while True:
 print('Digite se nome e idade (ex: João 25):')
 nome, idade = input().split()
 idade = int(idade)

 if idade < 16:
    print(f'\n{nome}, você não pode votar.')
    
 elif idade >= 16 and idade < 18:
    print(f'\n{nome}, você pode votar, mas não é obrigatório.')
    escolha = input('Deseja votar? (s/n): ')
    if escolha == "s": 
     voto = input('\nDigite o número do seu candidato:')
    if voto.isnumeric() == True:
     print(f'Você votou em {voto}, obrigado por votar.')
    elif escolha == "n":
     print('Você optou por não votar.')
   
    else:
        print('Número do candidato inválido. Por favor, digite um número válido.')    
                                                                              
 if idade >= 18:
    print(f'\n{nome}, você é obrigado a votar.')
    voto = input('\nDigite o número do seu candidato:')
    if voto.isnumeric() == True:
        print(f'Você votou em {voto}, obrigado por votar.')
    else:
        print('Número do candidato inválido. Por favor, digite um número válido.')                                                                          
    
    
 print('\nFim do programa.')
 print('\n' * 4)
    
    
    
    
    
    
    