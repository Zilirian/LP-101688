from os import system
system('cls')

# Variáveis para armazenar as estatísticas
numeros = []
quantidade_pares = 0
quantidade_impares = 0
soma_impares = 0
soma_pares = 0
soma_geral = 0
quantidade_positivos = 0
quantidade_negativos = 0
media = 0

# Processando cada número
def negativo_positivo(numero):
    if numero > 0:
        return 'Positivo'
    elif numero < 0:
        return 'Negativo'
    else:
        return 'Zero'

def par_impar(numero):
    if numero % 2 == 0:
        return 'Par'
    else:
        return 'Ímpar'
    
def maior_menor(lista):
    if len(lista) == 0:
        return None, None
    return max(lista), min(lista)

# Calculando as médias
def media_geral(soma, quantidade):
        return soma / quantidade

def main(): 
    # Variável para armazenar os números
    for i in range(5):
        numeros.append(int(input(f"Digite o {i+1}º número: ")))
    quantidade_total = len(numeros)
    soma_geral = sum(numeros)
    quantidade_positivos = sum(1 for num in numeros if num > 0)
    quantidade_negativos = sum(1 for num in numeros if num < 0)
    quantidade_pares = sum(1 for num in numeros if num % 2 == 0)
    quantidade_impares = sum(1 for num in numeros if num % 2 != 0)
    maior, menor = maior_menor(numeros)
    media = media_geral(soma_geral, quantidade_total)
    # Imprimindo as estatísticas
    print("\nEstatísticas dos números:")
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")
    print(f"Quantidade de pares: {quantidade_pares}")
    print(f"Quantidade de ímpares: {quantidade_impares}")
    print(f"Quantidade de positivos: {quantidade_positivos}")
    print(f"Quantidade de negativos: {quantidade_negativos}")
    print(f'A média geral é: {media}')

if __name__ == '__main__':
    main()