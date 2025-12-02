from random import randint
from time import sleep

lista = []
jogos = []
print('-' * 35)
print(f'{'PALPITES JOGOS MEGA SENA':^35}')
print('-' * 35)
quant = int(input('Quantos palpites voçê quer? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 61)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*4,f' SORTEANDO {quant} JOGOS ','-='*4)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    if quant < 10:
        sleep(0.5)
    elif quant < 20:
        sleep(0.3)
print('-='*5,'BOA SORTE', '-='*5)


