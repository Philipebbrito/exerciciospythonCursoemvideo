def aumentar(n = 0, taxa = 0, formato=False):
    res = n + (n * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(n = 0, taxa = 0, formato=False):
    res = n - (n * taxa/100)
    return res if formato is False else moeda(res)


def dobro(n = 0, formato=False):
    dobro = n * 2
    return dobro if formato is False else moeda(dobro)


def metade(n = 0, formato=False):
    met = n / 2
    return met if formato is False else moeda(met)

def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:>7.2f}'.replace('.',',')
