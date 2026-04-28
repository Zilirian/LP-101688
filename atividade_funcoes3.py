from os import system as sy
sy('cls')
from time import sleep

def limpar_tela():
    sy('cls')
   
lista_usuarios = []
class conta_bancaria:
    def __init__(self, us='', sd=0):
        self.usuario = us
        self.saldo = sd

    def sacar(self):
        limpar_tela()
        try:
            pedido = float(input('Digite o valor desejado do saque: '))
            if pedido <= self.saldo:
                self.saldo -= pedido
                print('Saque efetuado com sucesso!')
            else:
                print('Saldo insuficiente para o saque.')
        except ValueError:
            print('Valor inválido para saque.')
        sleep(3)
        limpar_tela()

    def depositar(self):
        try:
            pedido = float(input('Digite o valor desejado do depósito: '))
            self.saldo += pedido
            print('Depósito efetuado com sucesso!')
        except ValueError:
            print('Valor inválido para depósito.')
        sleep(3)
        limpar_tela()

    def mostrar_saldo(self):
        print(f'Saldo do {self.usuario}: {self.saldo:.2f}')
        sleep(3)
        limpar_tela()


def validar_opcao(opcao):
    return 1 <= opcao <= 5


def menu():
    print('''
            -------------MENU-------------
            1 - Criar usuário
            2 - Sacar
            3 - Depositar
            4 - Saldo
            5 - Sair
          ''')
    while True:
        try:
            opcao = int(input('Digite a opção desejada: '))
            if validar_opcao(opcao):
                break
            else:
                print('Digite um código válido')
                sleep(3)
                limpar_tela()
        except ValueError:
            print('Digite um número válido')
            sleep(3)
            limpar_tela()
    return opcao


def selecionar_conta():
    if not lista_usuarios:
        print('Nenhum usuário cadastrado.')
        sleep(3)
        limpar_tela()
        return None

    nome = input('Digite o nome do usuário: ')
    for conta in lista_usuarios:
        if conta.usuario == nome:
            return conta

    print('Usuário não encontrado.')
    sleep(3)
    limpar_tela()
    return None


def criar_usuario():
    nome = input('Digite o nome do usuário: ')
    conta = conta_bancaria(nome, 0)
    lista_usuarios.append(conta)
    print('Usuário criado com sucesso!')
    sleep(3)
    limpar_tela()


def sacar_usuario():
    conta = selecionar_conta()
    if conta:
        conta.sacar()


def depositar_usuario():
    conta = selecionar_conta()
    if conta:
        conta.depositar()


def ver_saldo():
    conta = selecionar_conta()
    if conta:
        conta.mostrar_saldo()


def filtro_opcao(opcao):
    match opcao:
        case 1:
            criar_usuario()
        case 2:
            sacar_usuario()
        case 3:
            depositar_usuario()
        case 4:
            ver_saldo()
        case 5:
            print('Encerrando sistema...')
            exit()
        case _:
            print('Opção inválida.')


def main():
    while True:
        opcao = menu()
        filtro_opcao(opcao)


if __name__ == '__main__':
    main()