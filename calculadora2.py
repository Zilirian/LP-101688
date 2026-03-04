import os
os.system("cls || clear")
while True:
    
 print('\n\n---calculadora_simples---\n')
 print('Digite a operação (ex: 2 + 3): ')
 a, operacao, b = input().split()
 a = float(a)
 b = float(b)
 resultado = 0
 
 match operacao:
  case  "+":
     resultado = a + b
  case "-":
     resultado = a - b
  case "*":
     resultado = a * b
  case "/":
     resultado = a / b
  case _:
     print("Operação inválida.")
     continue
 

 print(f'Resultado: {resultado:.2f}')