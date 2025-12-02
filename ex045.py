import time
from random import randint


itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('''Suas opçôes: 
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua jogada: '))

print('\033[0;34mJO')
time.sleep(0.5)
print('\033[0;34mKEN')
time.sleep(0.5)
print('\033[0;34mPO\033[0m')
time.sleep(0.5)

print('='*30)
print(f'Computador jogou: {itens[computador]}')
print(f'Jogador jogou: {itens[jogador]}')
print('='*30)

if computador == 0: #jogou pedra
    if jogador == 0:
        print('\033[44m EMPATE \033[0m')
    elif jogador == 1:
        print('\033[42m JOGADOR GANHOU \033[0m')
    elif jogador == 2:
        print('\033[1;101m\033[1;97m COMPUTADOR GANHOU \033[0m')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1: #jogou papel
    if jogador == 0:
        print('\033[1;101m\033[1;97m COMPUTADOR GANHOU \033[0m')
    elif jogador == 1:
        print('\033[44m EMPATE \033[0m')
    elif jogador == 2:
        print('\033[42m JOGADOR GANHOU \033[0m')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: #jogoutesoura
    if jogador == 0:
        print('\033[42m JOGADOR GANHOU \033[0m')
    elif jogador == 1:
        print('\033[1;101m\033[1;97m COMPUTADOR GANHOU \033[0m')
    elif jogador == 2:
        print('\033[44m EMPATE \033[0m')
    else:
        print('JOGADA INVALIDA')
