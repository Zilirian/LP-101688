import os
os.system('cls || clear')

print('Quntas maçãs você deseja comprar?')
quantidade = int(input())

if quantidade < 12:
    preco = 1.30
elif quantidade >= 12:
    preco = 1.00
    
total = quantidade * preco
print(f'\nO preço total é: R${total:.2f}')
print('\n' * 4)