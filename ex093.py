"""jogador = {}

jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"].capitalize()} jogou? '))

gols = []
total = 0
media = 0

for c in range(partidas):
    gol = int(input(f'Quantos gols na partida {c+1}: '))
    gols.append(gol)
    total += gol

jogador['gols'] = gols
jogador['total'] = total

print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')

print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for k, v in enumerate(jogador['gols']):
    print(f'Na partida {k+1}, fez {v} gols.')
print(f'Foi um total de {jogador['total']} gols.')
print(f'Com uma média de {total / partidas} gols.')"""

jogador = dict()
partidas = []
gols = 0
total = 0
media = 0
jogador['nome'] = str(input('Nome do Jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"].upper()} jogou?: '))
for c in range(tot):
    partidas.append(int(input(f'   Quantos gols na partida {c+1}?')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f' - {k} tem valor {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"].upper()} jogou {len(jogador["gols"])} partidas.')
for k, v in enumerate(jogador['gols']):
    print(f' - Na partida {k+1}, {jogador["nome"].upper()} fez {v} gols')
print('=-'*30)
print(f'Fez o total de {jogador["total"]} gols.')
print(f'Com uma média de {jogador["total"] / tot} gols')