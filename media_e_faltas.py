import os
os.system('cls || clear)')

print('Digite o número de faltas do aluno:')
faltas = int(input())
print('Digite a primeira nota do aluno:')
nota1 = float(input())
print('Digite a segunda nota do aluno:')
nota2 = float(input())
print('\n')

media = (nota1 + nota2) / 2
if media >= 7 and faltas <= 40:
     print(f'O aluno foi aprovado')
else:
    print('Aluno reprovado')