def aumentar(n = 0, taxa = 0):
    res = n + (n * taxa/100)
    return res


def diminuir(n = 0, taxa = 0):
    res = n - (n * taxa/100)
    return res


def dobro(n = 0):
    dobro = n * 2
    return dobro


def metade(n = 0):
    met = n / 2
    return met

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:>7.2f}'.replace('.',',')
