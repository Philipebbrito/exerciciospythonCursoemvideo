galera = []
pessoa = {}
lista = []
somaidades = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor digite apenas "M ou F".')
    pessoa['idade'] = int(input('Idade: '))
    somaidades += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas "S ou N".')
    if resp == 'N':
        break
print('=-'*30)
print(f' - Ao todo temos {len(galera)} pessoas cadastradas!')
print(f'A média das idades é de {somaidades / len(galera):.2f} anos.')
print(f'As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"].upper()} ', end='')
print()
print(f'Lista das pessoas que estão acima da média de idade:', end='')
for p in galera:
    if p['idade'] >= (somaidades / len(galera)):
        print(f'   ')
        for k, v in p.items():
            print(f'{k.capitalize()} = {v}: ', end='')
        print()
print('<<<   ENCERRADO   >>>')