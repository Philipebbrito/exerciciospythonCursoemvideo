from random import randint
from time import sleep

def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(1, 11)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares da lista {lista}, temos {soma}.')


def somaimpar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 1:
            soma += valor
    print(f'Somando os valores ímpares da lista {lista}, temos {soma}.')


numeros = []
sorteia(numeros)
somapar(numeros)
somaimpar(numeros)