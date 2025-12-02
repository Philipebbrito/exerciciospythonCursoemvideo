valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não adicionado!')
    continuar = input('Deseja continuar? [S/N]').strip().upper()[0]
    if continuar == 'N':
        break
valores.sort()
print('*'*45)
print(f'Os valores digitados foram: {valores}')
