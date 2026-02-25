import os
os.system('cls || clear')

print('Digite um número:')
num1 = float(input())
print('Digite outro número:')
num2 = float(input())

print(f'\nOs números escolhidos foram: {num1} e {num2}')
print('O maior número é:', max(num1, num2))
print('O menor número é:', min(num1, num2))

print('\nFim do programa.')
print('\n' * 4)
