import os
os.system('cls || clear')

# criando um vetor
vetor_notas = []
QUANTIDADE_DE_NOTAS = 5

print('Adicionando 3 notas.')
for i in range(QUANTIDADE_DE_NOTAS):
    nota = float(input(f'Digite a {i + 1}ª nota: '))
    vetor_notas.append(nota)
    
print('\nExibindo resultados:')
# for Each - é quando você quer percorrer um vetor, ou seja, uma coleção de dados, e fazer algo com cada um desses dados.
# enumerate = através da variável i, numera a quantidade de repetições
for i, uma_nota in enumerate(vetor_notas, start =1):
    print(f'{i}º Nota: {uma_nota:.2f}')
    
    # pra que o print serve - 