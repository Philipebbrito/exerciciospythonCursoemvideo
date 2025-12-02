'''Exercício Python 104: Crie um programa que tenha
 a função leiaInt(), que vai funcionar de forma semelhante ‘
 a função input() do Python, só que fazendo a validação
 para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite
 um n: ‘'''
def leiaint(msg):
    ok = False
    valor = 0
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[31mERRO! Por favor digite um número inteiro válido!\033[0m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário!\033[0m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número real válido!\033[0m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida!\033[0m')
            return 0
        else:
            return n


#PROGRAMA PRINCIPAL
while True:
    nint = leiaint('Digite um número inteiro: ')
    nfloat = leiafloat('Digite um número real: ')
    print(f'Voçê digitou o número inteiro {nint} e o real {nfloat}')

