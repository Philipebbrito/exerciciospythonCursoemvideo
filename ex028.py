import random
import time
computador = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(3)
if computador == jogador:
    print('PARABÉNS! Voçê acertou!')
else:
    print('Não foi dessa vez! Tente Novamente!')