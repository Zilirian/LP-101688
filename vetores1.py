import os
os.system('cls || clear')


lista = []

for i in range(3):
    nota = float(input('Digite sua nota: '))
    lista.append(nota)
    
média = sum(lista) / len(lista)  
    
    
print(f'As média é: {média}')
