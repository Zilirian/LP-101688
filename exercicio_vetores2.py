import os
os.system('cls || clear')

notas = []
QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f'Digite a {i + 1}ª nota: \n'))
    notas.append(nota)
print()    
media = sum(notas) / QUANTIDADE_NOTAS
for i, uma_nota in enumerate(notas, start=1):
    print(f'{i}° nota: {uma_nota:.2f}')
   
if media >= 7:
    print(f'\nSua {i}° nota é {uma_nota}, parabéns você foi aprovado com média {media:.2f}.')
elif media >= 5:
    print(f'\nSua {i}° nota é {uma_nota}, você está de recuperação com média {media:.2f}.')
else:
    print(f'\nSua {i}° nota é {uma_nota}, infelizmente você foi reprovado com média {media:.2f}.')

     
