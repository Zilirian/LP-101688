import os
os.system('cls || clear')

print('Digite um número inteiro:')
num1 = int(input())
print('Digite outro número inteiro:')
num2 = int(input())

media = (num1 + num2) / 2
soma = num1 + num2
produto = num1 * num2
menor = min(num1, num2)
maior = max(num1, num2)

print('\nResultados:')
print(f'Média: {media}')
print(f'Soma: {soma}')
print(f'Produto: {produto}')
print(f'Menor: {menor}')
print(f'Maior: {maior}')
if num1 == num2:
    print('Os números são iguais.')
else:
    print('Os números são diferentes.')
print('\nFim do programa.')
print('\n' * 4)
    