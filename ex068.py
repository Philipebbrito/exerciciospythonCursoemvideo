vit = 0
from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*15)
while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou impar? [P/I]:')).strip().upper()[0]
    print(f'Voçê jogou {jogador} e o computador jogou {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            tipo = 'Par'
            print('Voçê venceu!!')
            vit += 1
        else:
            print('Voçê perdeu!!!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            tipo = 'Impar'
            print('Voçê venceu!!!')
        else:
            print('Voçê perdeu!!!')
            break
        print('Vamos jogar novamente!')
print(f'GAME OVER!!! Voçê ganhou {vit} vezes')

