time = []
jogador = dict()
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"].upper()} jogou?: '))
    partidas.clear()
    for c in range(tot):
        partidas.append(int(input(f'   Quantos gols na partida {c+1}?')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas "S ou N"!')
    if resp == 'N':
        break
print('=-'*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d).upper():<15}', end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! opção inválida!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"].upper()}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} {time[busca]["nome"].upper()} fez {g} gols.')
    print('-'*40)
print('  -- VOLTE SEMPRE --  ')