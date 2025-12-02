'''import random
computador = random.randint(0, 10)
jogador = 0
while computador != jogador:
    print('O computador vai pensar em um número entre 0 e 10. Tente adivinhar... ')
    jogador = int(input('Em que número eu pensei? '))
    if computador == jogador:
        print('PARABÉNS! Voçê acertou!')
    else:
        print('Não foi dessa vez! Tente Novamente!')'''
import random
computador = random.randint(0,10)
print('Sou seu computador ... Acabei de pensar em umnúmero entre 0 e 10')
print('Será que voçê consegue adivinhar qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais ... Tente novamente!')
        elif jogador > computador:
            print('Menos ... Tente novamente!')
print(f'ACERTOU!!! com {palpite} tentativas!')

