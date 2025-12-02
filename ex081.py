valores = []
while True:
    valor = int(input(f'Digite um valor: '))
    valores.append(valor)
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if continuar == 'N':
        break
tem5 = 5 in valores
print('=-'*30)
print(f'Valores digitados: {valores}')
print(f'Valores digitados em ordem crescente: {sorted(valores)}')
print(f'Valores digitados em ordem decrescente: {sorted(valores, reverse=True)}')
print(f'O valor 5 {'foi' if tem5 else 'não foi'} digitado')