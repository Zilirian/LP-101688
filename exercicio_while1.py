import os
os.system('cls || clear')

while True:
    print('\nDigite uma nota entre 0 e 10')
    num = float(input())
    if num >= 0 and num <= 10:
        print(f'A nota é {num}')
        break
    else:
        print('Tente novamente')
        
    