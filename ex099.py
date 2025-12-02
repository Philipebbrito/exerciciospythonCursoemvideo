def maior(* num):
    cont = maior = 0
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores e o maior valor é {maior}.')
    print('~~'*50)

maior(9,7,5,4,8,5,4,4)