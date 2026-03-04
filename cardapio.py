import os
os.system('cls || clear')

print('Bem vindo ao nosso restaurante, escolha o código correspondente ao prato desejado')
print("""
      ===============MENU===============   
      1        Picanha         R$ 25,00
      2        Lasanha         R$ 20,00
      3        Strogonoff      R$ 18,00
      4        Bife Acebolado  R$ 15,00
      5        Pão com ovo     R$  5,00
      
      """)
codigo = input('Digite o código do prato escolhido: ')
match codigo:
    case "1":
        print('Você escolheu Picanha, o valor é R$ 25,00')
    case "2":
        print('Você escolheu Lasanha, o valor é R$ 20,00')
    case "3":
        print('Você escolheu Strogonoff, o valor é R$ 18,00')
    case "4":
        print('Você escolheu Bife Acebolado, o valor é R$ 15,00')
    case "5":
        print('Você escolheu Pão com ovo, o valor é R$ 5,00')
    case _:
        print('Código inválido, por favor escolha um código entre 1 e 5.')
        
print("""
      =======PROGRAMA FINALIZADO========
      """)    