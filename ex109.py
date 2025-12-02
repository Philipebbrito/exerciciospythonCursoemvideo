import moeda2

valor = float(input('Digite um valor em R$ '))
print(f'A metade de {moeda2.moeda(valor)} é {moeda2.metade(valor, True)}')
print(f'O dobro de {moeda2.moeda(valor)} é {moeda2.dobro(valor, True)}')
print(f'Aumentando 10% de {moeda2.moeda(valor)} o resultado é {moeda2.aumentar(valor, 10, True)}')
print(f'Reduzindo 10% de {moeda2.moeda(valor)} o resultado é {moeda2.diminuir(valor, 10, True)}')