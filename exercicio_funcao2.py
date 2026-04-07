from os import system
system('cls')

def par_impar(num):
    if num % 2 == 0:
        return "par"
    else:
        return "ímpar"
def main():
    while True:
        try:
            num = int(input('Digite um n° inteiro: '))
            break
        except:
            system('cls')
            print('Deve ser um número e deve ser inteiro\n')
            continue
    system('cls')
    print(f'O número é: {par_impar(num)}')

main()