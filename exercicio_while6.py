import os
os.system('cls || clear')

print('''------------------MENU------------------
         1 --------------Picanha----------R$25.00
         2 --------------Lasanha----------R$20.00
         3 --------------Strogonoff-------R$18.00
         4 --------------Bife Acebolado---R$15.00
         5 --------------Pão com ovo------R$05.00
      ''')

valor_total = 0
while True:
    print('\nDigite o número do prato desejado')
    prato = int(input())
    match prato:
        case 1:
            print(f'\nO valor do prato é R$15.00')
        case 2:
            print('\nO valor do prato é R$20.00')
            valor_total += 20.00
        case 3:
            print('\nO valor do prato é R$18.00')
            valor_total += 18.00
        case 4:
            print('\nO valor do prato é R$15.00')
            valor_total += 15.00
        case 5:
            print('\nO valor do prato é R$05.00')
            valor_total += 5.00
        case _:
            print('\nNúmero do prato inválido, tente novamente')
    
    repeticao = input('\nVocê deseja escolher outro prato? (S/N)\n').upper()
    if repeticao == 'N':
        break
    
print(f'\nO valor total a ser pago é {valor_total:.2f}')

    