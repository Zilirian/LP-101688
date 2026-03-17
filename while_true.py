import os
os.system('cls || clear')

while True:
    idade= int(input('digite sua idade:'))
    if idade <= 18:
        print('Acesso negado')
        print('Tente novamente\n')
    else:
        print('Acesso permitido')   
        break
    
print('Fim')