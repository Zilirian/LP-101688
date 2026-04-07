from os import system
system('cls')

QUANTIDADE_NOTAS = 2
def _media(nt1, nt2):
    return (nt1 + nt2) / QUANTIDADE_NOTAS

def _validacao(media):
    if media >= 7:
        return "aprovado"
    else:
        return "reprovado"
    
def main():
    while True:
        
        try:
            nt1 = float(input('Digite a 1° nota: '))
            nt2 = float(input('Digite a 2° nota: '))
            break
        except:
            system('cls')
            print('Deve ser um número\n')
            continue
    media = _media(nt1, nt2)
    print(f'O aluno está {_validacao(media)}')

main()