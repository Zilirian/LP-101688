import os
os.system('cls || clear')

vetor_nome_pratos = []
vetor_preco_pratos = []
preco_pratos = 0

while True:
    print('Digite o número correspondente ao prato desejado')
    menu = int(input('''
          ----------------------MENU-------------------------
           1 - Picanha - R$25.00
           2 - Lasanha -  R$20.00
           3 - Strogonoff -  R$18.00
           4 - Bife Acebolado -  R$15.00
           5 - Pão com ovo -  R$5.00
           
           0 - Sair \n
          '''))
    match menu:
        case 1:
            print('\nVocê escolheu Picanha.')
            preco_pratos += 25
            vetor_nome_pratos.append('Picanha')
            vetor_preco_pratos.append(25)
        case 2:
            print('\nVocê escolheu Lasanha.')
            preco_pratos += 20
            vetor_nome_pratos.append('Lasanha')
            vetor_preco_pratos.append(20)
        case 3:
            print('\nVocê escolheu Strogonoff.')
            preco_pratos += 18
            vetor_nome_pratos.append('Strogonoff')
            vetor_preco_pratos.append(18)
        case 4:
            print('\nVocê escolheu Bife Acebolado.')
            preco_pratos += 15
            vetor_nome_pratos.append('Bife Acebolado')
            vetor_preco_pratos.append(15)
        case 5:
            print('\nVocê escolheu Pão com ovo.')
            preco_pratos += 5
            vetor_nome_pratos.append('Pão com ovo')
            vetor_preco_pratos.append(5)
        case 0:
            print('\nPrograma encerrado.')
            break
        case _:
            print('\nOpção inválida')
            break
    escolha = input('Você deseja pedir outro prato? (S/N) ').lower()
    match escolha:
        case "s":
            continue
        case 'n':
            break
        case _:
            print('opção inválida')
            continue

    
print(f'\nOs pratos pedidos foram {vetor_nome_pratos}')
print(f'O preço final foi R${preco_pratos}')
        
        