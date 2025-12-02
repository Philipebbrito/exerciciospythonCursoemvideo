def aumentar(n = 0, taxa = 0, formato=False):
    res = n + (n * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(n = 0, taxa = 0, formato=False):
    res = n - (n * taxa/100)
    return res if formato is False else moeda(res)


def dobro(n = 0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def metade(n = 0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)

def moeda(n = 0, cifrao = 'R$'):
    return f'{cifrao}{n:>7.2f}'.replace('.',',')


def resumo(valor, aumento=10, reducao=5):
    """Exibe um resumo do valor e suas operações."""
    print("-" * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print("-" * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor, True)}')
    print(f'Metade do preço: \t{metade(valor, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(valor, reducao, True)}')
    print("-" * 30)