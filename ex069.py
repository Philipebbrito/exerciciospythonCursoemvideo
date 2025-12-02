cont = maior = homem = mulher = 0
while True:
    print('='*20)
    print('CADASTRE UMA PESSOA')
    print('='*20)
    idade = int(input('Idade: '))
    sexo = ' '
    perg = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('='*20)
    while perg not in 'SsNn':
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if idade >= 18:
        cont += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff':
        if idade < 20:
            mulher += 1
    if perg in 'Nn':
        break
print('='*30)
print(f'{cont} Pessoas com mais de 18 anos!')
print(f'{homem} Homens cadastrados!')
print(f'{mulher} Mulheres com menos de 20 anos!')