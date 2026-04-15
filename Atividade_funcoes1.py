import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []

def classificacao(imc):
        if imc >= 40:
            return 'Obesidade Grau III (Mórbida)'
        elif imc >= 35 and imc <= 39.9:
            return 'Obesidade Grau II (Severa)'
        elif imc >= 30 and imc <= 34.9:
            return 'Obesidade Grau I'
        elif imc >= 25 and imc <= 29.9:
            return 'Sobrepeso'
        elif imc >= 18.5 and imc <= 24.9:
            return 'Peso ideal'
        elif imc >= 17 and imc <= 18.4:
            return 'Abaixo do Peso'
        
def transformacao(peso, altura):
    return peso / (altura ** 2) 

def main():
    # Solicitando os dados dos usuários em um loop
    while True:
        logoSenai()
        nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
        
        # Verificando se o usuário quer sair
        if nome.lower() == 'sair':
            break
        
        idade = int(input("Digite a idade do usuário: "))
        altura = float(input("Digite a altura do usuário (em metros): "))
        peso = float(input("Digite o peso do usuário (em quilogramas): "))
        
        # Adicionando os dados às listas
        nomes.append(nome)
        idades.append(idade)
        alturas.append(altura)
        pesos.append(peso)
        os.system('cls')

        imc = [transformacao(a, b) for a, b in zip(pesos, alturas) ]
        classificacao_imc = [classificacao(x) for x in imc]


    # Exibindo os dados armazenados
    logoSenai()
    print("\nDados dos usuários:")
    for i in range(len(nomes)):
        print(f"Usuário {i+1}:")
        print("Nome:", nomes[i])
        print("Idade:", idades[i])
        print("Altura:", alturas[i], "metros")
        print("Peso:", pesos[i], "quilogramas")
        print(f"Seu imc é: {imc[i]:.2f}")
        print(f"Sua classificação é: {classificacao_imc[i]}")
        print('\n')
        

main()