import os
os.system('cls || clear')

print('Digite seu sexo')
sexo = input().lower()
print('Digite seu ano de nascimento')
nascimento = int(input())

idade = 2026 - nascimento
idade_obrigatoria = idade >= 18
sexo_obrigatorio = sexo == 'masculino'
if sexo_obrigatorio and idade_obrigatoria:
    print('Você deve se alistar')
else:
    print('Você não precisa se alistar')