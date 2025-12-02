anonasc = int(input('Digite o ano de nascimento: '))
idade = 2025 - anonasc
if idade <= 0:
    print('TENTE NOVAMENTE!!!')
else:
    print(f'O atleta tem {idade} anos')
if idade > 25:
    print('Classificação: MASTER')
elif idade > 19 and idade <= 25:
    print('Classificação: SÊNIOR')
elif idade > 14 and idade <= 19:
    print('Classificação: JÚNIOR')
elif idade > 9 and idade <= 14:
    print('Classificação: INFANTIL')
elif idade > 0 and idade <= 9:
    print('Classificação: MIRIM')
else:
    print('TENTE NOVAMENTE!!!')