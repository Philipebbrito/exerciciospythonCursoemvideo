tot = totmil = menor = cont = 0
barato = ''
print('='*30)
print('----- LOJA SUPER BARATÃO -----')
print('='*30)
while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    cont += 1
    tot += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    res = ' '
    while res not in 'SsNn':
        res = str(input('Quer continuar?: [S/N]')).strip().upper()[0]
    print('=-'*15)
    if res in 'Nn':
        break
print('-'*8,'FIM DO PROGRAMA','-'*15)
print(f'O total gasto foi de R${tot:.2f}.')
print(f'Temos {totmil} produto que custa mais de R$1.000.')
print(f'O produto mais barato custa R${menor:.2f}. O produto mais barato é o {barato}')
