import os
os.system('cls || clear')
import time

quantidade_pessoas = 0
quantidade_mulheres = 0
salario_apartir5000 = 0
total_salario = 0
total_idades = []
while True:
    
    
    
    print('''
          -----------------------MENU-----------------------
          Adicionar pessoa                        - Digite 1
          Exibir resultados                       - Digite 2
          Sair                                    - Digite 3
          ''')
    opcao = int(input('Digite a opção desejada: '))
    match opcao:
        case 1:
            quantidade_pessoas += 1
            print('Opção 1 selecionada: Adicionar pessoa')  # Lógica para adicionar pessoa 
            nome = input('Digite seu nome:')
            idade = int(input('Digite sua idade:'))
            total_idades.append(idade)
            sexo = input('Digite seu sexo (M/F):')
            if sexo.lower() == 'f':
                quantidade_mulheres += 1
            salario = float(input('Digite seu salário:'))
            if salario >= 5000 and sexo.lower() == 'f':
                salario_apartir5000 += 1
                total_salario += salario
            time.sleep(1.5)
            os.system('cls || clear')
            
        case 2:
            maior_idade = max(total_idades)
            menor_idade = min(total_idades)
            
            print('Opção 2 selecionada: Exibir resultados')  # Lógica para exibir resultados
            print(f'Quantidade de pessoas cadastradas: {quantidade_pessoas}')
            print(f'A média dos salários é: {total_salario / quantidade_pessoas:.2f}')
            print(f'A menor idade do grupo é: {menor_idade}, e a maior idade do grupo é: {maior_idade}')
            print(f' {salario_apartir5000} mulheres ganham a partir de R$5000,00')
            time.sleep(10)
            os.system('cls || clear')
        case 3:
            print('Opção 3 selecionada: Sair')
            break
        case _:
            print('Opção inválida. Por favor, tente novamente.')
            
print('Programa encerrado. Obrigado por usar o sistema!')