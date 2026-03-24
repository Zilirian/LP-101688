import os
os.system('cls || clear')
import time

    
total_familias = 0
total_numero_filhos = 0
media_numero_filhos = 0
min_max_salarios = []
total_salarios = 0

while True:
    print('''
          -----------------------MENU-----------------------
          Adicionar família                       - Digite 1
          Sair e exibir resultados                - Digite 2
            ''')
    
    opcao = int(input('Digite a opção desejada: '))
    match opcao:
        case 1:
            total_familias += 1
            print('Opção 1 selecionada: Adicionar família')  # Lógica para adicionar pessoa 
            print('Digite o salário da família:')
            salario = float(input())
            total_salarios += salario
            min_max_salarios.append(salario)
            print('Digite o número de filhos da família:')
            numero_filhos = int(input())
            total_numero_filhos += numero_filhos
            criancas_por_familia_media = total_numero_filhos / total_familias
            os.system('cls || clear')
            media_salario = total_salarios / total_familias
            time.sleep(2)
        case 2:
            media_salario = total_salarios / total_familias
            print('Opção 2 selecionada: Sair e exibir resultados')  # Lógica para exibir resultados
            print(f'Quantidade de famílias cadastradas: {total_familias}')
            print(f'A média dos salários é: {media_salario:.2f}')
            print(f'A média do número de filhos por família é: {criancas_por_familia_media:.2f}')
            print(f'O maior salário entre as famílias é: {max(min_max_salarios):.2f} e o menor salário entre as famílias é: {min(min_max_salarios):.2f}')
            time.sleep(10)
            os.system('cls || clear')
            break
            
            
        case _:
            print('Opção inválida. Por favor, tente novamente.') 