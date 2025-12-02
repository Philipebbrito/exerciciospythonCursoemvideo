lista = []
dado = []
pesado = leve = 0

while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: Kg')))
    if len(lista) == 0:
        pesado = leve = dado[1]
    else:
        if dado[1] > pesado:
            pesado = dado[1]
        if dado[1] < leve:
            leve = dado[1]

    lista.append(dado[:])
    dado.clear()

    res = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if res in 'Nn':
        break
    print('-=' * 20)

print('=-'*20)
print(f'{len(lista)} pessoas cadastradas')
print(f'O maior peso foi de {pesado} Kg, peso de: ')
for p in lista:
    if p[1] == pesado:
        print(f'{p[0].capitalize()}')
print(f'O menor peso foi de {leve} Kg, peso de: ')
for p in lista:
    if p[1] == leve:
        print(f'{p[0].capitalize()}')