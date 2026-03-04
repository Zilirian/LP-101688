import os
os.system('cls || clear')


print('Digite um dia da semana')
dia = input().lower()
match dia:
    case "segunda":
        print("Hoje é segunda-feira")
    case "terça":
        print("Hoje é terça-feira")
    case "quarta":
        print("Hoje é quarta-feira")
    case "quinta":
        print("Hoje é quinta-feira")
    case "sexta":
        print("Hoje é sexta-feira")
    case "sábado":
        print("Hoje é sábado")
    case "domingo":
        print("Hoje é final de semana") 
    case _:
        print("Dia inválido")
        
print(dia)

print("\n===FIM===")