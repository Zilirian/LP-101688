import os
os.system('cls || clear')
import time
QUANTIDADE_NOTAS = 3
notas = []
for i in range(QUANTIDADE_NOTAS):
    print('\nDigite uma nota:')
    nota = float(input())
    notas.append(nota)
    totalnums = sum(notas)

media = totalnums / QUANTIDADE_NOTAS
if media >= 7:
    print("Aprovado")
elif media >= 4:
    print("Recuperação")
else:
    print("Reprovado")
