import os
os.system('cls || clear')

logins_corretos = ["silas123", "maria456", "joao789"]
senhas_corretas = ["123456", "654321", "987654"]
tentativas = 0

while True:
    print('\nDigite seu login')
    login = input().lower()
    print('Digite sua senha')
    senha = input().lower()
    
    login_esta_correto = login in logins_corretos
    senha_esta_correta = senha in senhas_corretas
   
    if login_esta_correto and senha_esta_correta:
        print('\nLogin realizado com sucesso')
        break
    else:
        print('\nSenha ou login incorretos, tente novamente')
        tentativas += 1
        if tentativas == 3:
            print('Número de tentativas excedido, tente novamente mais tarde')
            break