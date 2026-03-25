import os
os.system('cls || clear')

while True:   
    import time
    vetor_num = []
    QUANTIDADE_NUM = 5

    for i in range(QUANTIDADE_NUM):
        num = int(input(f'Digite o {i + 1}º número: '))
        vetor_num.append(num)
    print()
    for i, um_num in enumerate(vetor_num, start=1):
        print(f'O {i}º número é {um_num}')
        
    print(f'\nO maior número do é {max(vetor_num)} e o menor {min(vetor_num)}\n')

    for i in range(4, 0, -1):
        print(f'Delentando o programa em {i} segundos...')
        time.sleep(1)
    os.system('cls || clear')

