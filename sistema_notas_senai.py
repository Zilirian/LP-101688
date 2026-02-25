import os
os.system('cls || clear')

print ('Bem-vindo ao sistema de notas do SENAI!')
print('\nDigite o nome do aluno:')
nome = input()
print('\nDigite a nota 1:')
nota1 = float(input())
print('\nDigite a nota 2:')
nota2 = float(input())

media = (nota1 + nota2) / 2
 
if media >= 9:
    conceito = 'A'
elif media >= 7.5 and media < 9:
    conceito = 'B'
elif media >= 6 and media < 7.5:
    conceito = 'C'
elif media >= 4 and media < 6:
    conceito = 'D'
elif media < 4:
    conceito = 'E'

if conceito in ['A', 'B', 'C']:
    situacao = 'Aprovado'
elif conceito in ['D', 'E']:
    situacao = 'Reprovado'   
    
print(f'\nAluno: {nome}, foi {situacao} com {conceito} e média {media:.2f}.') 
