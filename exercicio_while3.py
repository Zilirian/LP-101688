import os
os.system('cls || clear')
import time

LOGIN = "silas123"
SENHA = "123456"
while True:
    print('\nDigite seu login')
    login = input().lower()
    print('Digite sua senha')
    senha = input().lower()
    if login == LOGIN and senha == SENHA:
        print('\nLogin realizado com sucesso')
        break
    else:
        print('\nLogin ou senha incorretos, tente novamente')
        
# Também é possível usar no if/else o login_esta_correto = login == login_correto