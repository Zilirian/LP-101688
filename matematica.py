

import os
os.system('cls || clear')
while True:
 print('Digite uma conta matemática (ex: 2 + 3):')
 conta = input()
 num1, operador, num2 = conta.split()

 num1 = float(num1)
 num2 = float(num2)

 if operador == '+':
    resultado = num1 + num2
 elif operador == '-':
    resultado = num1 - num2
 elif operador == '*':
    resultado = num1 * num2
 elif operador == '/':
    resultado = num1 / num2
 else:
    print('Operador inválido.')
    exit()
    
 print(f'O resultado é: {resultado:.2f}') 
 print("\n" * 4)
 
    