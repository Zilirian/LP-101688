from os import system
from time import sleep

matriculas = []
senhas = []
salarios = []
vale_transportes = []
vale_refeicoes = []
dependentes = []


def limpar_tela():
    system('cls')


def ler_numero_inteiro(pergunta):
    while True:
        valor = input(pergunta)
        if valor.isdigit():
            return int(valor)
        print('Digite um número inteiro válido.')


def ler_valor_real(pergunta):
    while True:
        texto = input(pergunta).replace(',', '.')
        try:
            valor = float(texto)
            if valor >= 0:
                return valor
            print('O valor não pode ser negativo.')
        except ValueError:
            print('Digite um valor em reais válido, por exemplo 2500.00.')


def ler_sim_nao(pergunta):
    while True:
        resposta = input(pergunta).strip().lower()
        if resposta == 's':
            return True
        if resposta == 'n':
            return False
        print('Digite s para sim ou n para não.')


def menu():
    print('''
=======================MENU======================
1 - Registrar funcionário
2 - Calcular folha de pagamento
3 - Exibir funcionários cadastrados
4 - Encerrar programa
''')
    opcao = ler_numero_inteiro('Digite a opção desejada: ')
    return opcao


def registrar_funcionario():
    print('\n=== Registrar Funcionário ===')
    matricula = input('Digite a matrícula do funcionário: ').strip()
    senha = input('Digite a senha do funcionário: ').strip()
    salario = ler_valor_real('Digite o salário base (R$): ')
    recebe_vt = ler_sim_nao('Deseja receber vale transporte? (s/n): ')
    valor_vr = ler_valor_real('Digite o valor do vale refeição fornecido pela empresa (R$): ')
    dep = ler_numero_inteiro('Digite a quantidade de dependentes: ')

    matriculas.append(matricula)
    senhas.append(senha)
    salarios.append(salario)
    vale_transportes.append(1 if recebe_vt else 0)
    vale_refeicoes.append(valor_vr)
    dependentes.append(dep)

    print('\nFuncionário registrado com sucesso!')
    sleep(2)
    limpar_tela()


def buscar_funcionario(matricula, senha):
    for i in range(len(matriculas)):
        if matriculas[i] == matricula and senhas[i] == senha:
            return i
    return -1


def calcular_inss(salario):
    if salario <= 1518.00:
        return salario * 0.075
    elif salario <= 2793.88:
        return salario * 0.09
    elif salario <= 4190.83:
        return salario * 0.12
    elif salario <= 8157.41:
        return salario * 0.14
    else:
        return 951.62


def calcular_irrf(salario):
    if salario <= 2428.80:
        return 0.0
    elif salario <= 2826.65:
        return salario * 0.075
    elif salario <= 3751.05:
        return salario * 0.15
    elif salario <= 4664.68:
        return salario * 0.225
    else:
        return salario * 0.275


def calcular_vale_transporte(salario, recebe_vt):
    if recebe_vt:
        return salario * 0.06
    return 0.0


def calcular_vale_refeicao(valor_vr):
    return valor_vr * 0.20


def calcular_plano_saude(dep):
    return dep * 150.0


def exibir_folha(i):
    salario = salarios[i]
    recebe_vt = vale_transportes[i] == 1
    valor_vr = vale_refeicoes[i]
    dep = dependentes[i]

    inss = calcular_inss(salario)
    irrf = calcular_irrf(salario)
    vt = calcular_vale_transporte(salario, recebe_vt)
    vr = calcular_vale_refeicao(valor_vr)
    plano_saude = calcular_plano_saude(dep)
    salario_liquido = salario - inss - irrf - vt - vr - plano_saude

    print('\n=== Folha de Pagamento ===')
    print('Matrícula:', matriculas[i])
    print(f'Salário base: R$ {salario:.2f}')
    print('Recebe vale transporte:', 'Sim' if recebe_vt else 'Não')
    print(f'Valor do vale refeição: R$ {valor_vr:.2f}')
    print('Dependentes:', dep)
    print('\n--- Descontos ---')
    print(f'INSS: R$ {inss:.2f}')
    print(f'IRRF: R$ {irrf:.2f}')
    print(f'Vale transporte: R$ {vt:.2f}')
    print(f'Vale refeição: R$ {vr:.2f}')
    print(f'Plano de saúde: R$ {plano_saude:.2f}')
    print(f'\nSalário líquido: R$ {salario_liquido:.2f}')
    sleep(5)
    limpar_tela()


def exibir_funcionarios():
    if len(matriculas) == 0:
        print('\nNenhum funcionário cadastrado.')
    else:
        print('\n=== Funcionários Cadastrados ===')
        for i in range(len(matriculas)):
            print(f'{i+1}. Matrícula: {matriculas[i]} - Salário: R$ {salarios[i]:.2f}')
    sleep(5)
    limpar_tela()


def filtro_opcao(opcao):
    if opcao == 1:
        registrar_funcionario()
    elif opcao == 2:
        print('\n=== Acessar Folha de Pagamento ===')
        matricula = input('Digite a matrícula: ').strip()
        senha = input('Digite a senha: ').strip()
        indice = buscar_funcionario(matricula, senha)
        if indice >= 0:
            exibir_folha(indice)
        else:
            print('Matrícula ou senha incorretos.')
            sleep(2)
            limpar_tela()
    elif opcao == 3:
        exibir_funcionarios()
    elif opcao == 4:
        print('Encerrando programa...')
        sleep(2)
        return False
    else:
        print('Opção inválida. Digite um número entre 1 e 4.')
        sleep(2)
        limpar_tela()
    return True


def main():
    limpar_tela()
    continuar = True
    while continuar:
        opcao = menu()
        continuar = filtro_opcao(opcao)


if __name__ == '__main__':
    main()

