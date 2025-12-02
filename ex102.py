'''Exercício Python 102: Crie um programa que tenha
 uma função fatorial() que receba dois parâmetros:
 o primeiro que indique o número a calcular e outro
 chamado show, que será um valor lógico (opcional)
 indicando se será mostrado ou não na tela o processo
 de cálculo do fatorial.
'''
def fatorial(num, show=False):
    '''
    Calcula o fatorial de um número.
    :param num: Número a ser calculado.
    :param show: (opicional) Mostrar ou não o cálculo.
    :return: o valor do fatorial de um número.
    '''
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

valor = int(input('Digite um valor para ver seu fatorial: '))
print(fatorial(valor, show=True))
help(fatorial)