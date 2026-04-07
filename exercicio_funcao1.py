from os import system
system('cls')

def tabuada(num):
    for i in range(10):
        print(num * (i + 1))
while True:
    try:
        numero = int(input('Digite um n° inteiro'))
        break
    except:
        print('O n° deve ser inteiro')
        continue

def main():
    print('A tabuada do n° escolhido é:')
    tabuada(numero)

main()