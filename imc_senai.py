import os
os.system('cls || clear')
 
print('Bem vindo ao programa de cálculo do IMC!')
print('\nDigite seu peso em kg:')
peso = float(input())
print('\nDigite sua altura em metros:')
altura = float(input())

imc = peso / (altura ** 2) 

if imc >= 40:
    classificacao = 'Obesidade Grau III (Mórbida)'
elif imc >= 35 and imc <= 39.9:
    classificacao = 'Obesidade Grau II (Severa)'
elif imc >= 30 and imc <= 34.9:
    classificacao = 'Obesidade Grau I'
elif imc >= 25 and imc <= 29.9:
    classificacao = 'Sobrepeso'
elif imc >= 18.5 and imc <= 24.9:
    classificacao = 'Peso ideal parabéns'
elif imc >= 17 and imc <= 18.4:
    classificacao = 'Abaixo do Peso'
    
    

print(f'\nSeu IMC é: {imc:.2f} e sua classificação é: {classificacao}.')
print('Operação finalizada')
print('\n' * 4)