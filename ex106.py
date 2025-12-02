'''Exercício Python 106: Faça um mini-sistema que
utilize o Interactive Help do Python. O usuário vai
digitar o comando e o manual vai aparecer. Quando o usuário
digitar a palavra ‘FIM’, o programa se encerrará. Importante:
use cores.'''

from time import sleep


c = ('\033[m',
     '\033[0;31m',
     '\033[0;32m',
     '\033[0;33m',
     '\033[0;34m',
     '\033[44m',
     '\033[41m'
)

def ajuda(com):
    titulo(f'Acessando manual do comando {com}', 4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')
    sleep(2)

def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print(('~' * tam))
    print(c[0], end='')
    sleep(1)


#programa principal
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 1)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO' , 1)