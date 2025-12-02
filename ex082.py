lista = []
listapar = []
listaimpar = []
while True:
    valor = int(input(f'Digite um valor: '))
    lista.append(valor)
    if valor % 2 == 0:
        listapar.append(valor)
    elif valor % 2 == 1:
        listaimpar.append(valor)
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar in 'Nn':
        break
print('=-'*30)
print(f'A lista completa é {lista}')
print(f'Lista dos valores pares digitados {listapar}')
print(f'Lista dos valores pares digitados {listaimpar}')

