
import os
os.system("cls || clear")
 
print("Digite seu login:")
login = input()
print("Digite sua senha:")
senha = input()
senha_cadastrada = "cavalo123"
login_cadastrado = "marcelo"
login_correto = login == login_cadastrado
senha_correta = senha == senha_cadastrada


if login_correto and senha_correta:
     print("\nLogin bem-sucedido!")
else:
     print('\nLogin ou senha incorretos, tente novamente.')

print('\n' * 2)