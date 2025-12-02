import moeda

valor = float(input('Digite um valor: R$'))
print(f'A metade de R${valor} é R${moeda.dobro(valor)}')
print(f'Aumentando 10% de R${valor} o resultado é R${moeda.aumentar(valor, 10)}')
print(f'Reduzindo 10% de R${valor} o resultado é R${moeda.diminuir(valor, 10)}')