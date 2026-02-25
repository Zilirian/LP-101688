import os
os.system('cls || clear')

print('Bem vindo ao programa de aposentadoria do INSS')
print('Digite seu nome:')
nome = input()
print('Digite sua idade:')
idade = int(input())
print('Informe sua matrícula:')
matricula = input()
tempo_contribuicao = input('Digite seu tempo de contribuição (em anos):')
tempo_contribuicao = int(tempo_contribuicao)
nascimento = (2026 - idade)
if idade >= 65 or tempo_contribuicao >= 30 or (idade >= 60 and tempo_contribuicao >= 25):
    print(f'\n{nome}, você já pode se aposentar.')
    print('Você deseja se aposentar agora? (s/n):')
    escolha = input()
    if escolha == "s":
        print(f'Parabéns pela sua aposentadoria {nome}, nascido em {nascimento} com {idade}, cuja matricula é {matricula}! ')
    elif escolha == "n":
        print('Você optou por não se aposentar agora.')
    else:
        print('Opção inválida. Por favor, digite "s" para sim ou "n" para não.')
else:
    print(f'\n{nome}, você ainda não pode se aposentar.')
print('\nFim do programa.')