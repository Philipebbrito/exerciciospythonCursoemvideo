from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}a pessoa nasceu: '))
    idade = atual - nasc
    if idade > 21:
        totmaior += 1
        print('MAIOR DE IDADE!')
    else:
        totmenor += 1
        print('MENOR DE IDADE!')
    print(f'Essa pessoa tem {idade} anos')
print(f'Ao todos temos {totmaior} maiores de idade e {totmenor} menores de idade!')