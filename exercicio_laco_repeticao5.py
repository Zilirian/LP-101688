import os
os.system('cls || clear')
import time

notas = []
for i in range(4):
    print('\nDigite uma nota:')
    nota = float(input())
    notas.append(nota)
    totalnums = sum(notas)

media = totalnums / 4
print(media)

    