'''Exercício Python 103: Faça um programa que tenha
 uma função chamada ficha(), que receba dois parâmetros
 opcionais: o nome de um jogador e quantos gols ele marcou.
 O programa deverá ser capaz de mostrar a ficha do jogador,
 mesmo que algum dado não tenha sido informado corretamente.'''

def ficha(nome='DESCONHECIDO', gols=0):
    print(f'{nome.capitalize()} fez {gols} gols no campeonato!')


cont = tot = 0
while True:
    print('-='*20)
    n = str(input('Nome de jogador: '))
    g = str(input(f'Quantidade de gols de {n.upper()}: '))
    cont += 1
    if g.isnumeric():
        g = int(g)
        tot += g
    else:
        g = 0
    if n.strip() == '':
        ficha(gols=g)
    else:
        ficha(n, g)
    print('-='*20)
    resp = str(input('Quer continuar? [s/n]')).strip().upper()[0]
    if resp in 'Nn':
        break

print(f'{cont} Jogadores cadastrados!')
print(f'{tot} gols feitos no total!')