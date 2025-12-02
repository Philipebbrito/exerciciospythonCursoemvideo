tabela_brasileirao_serie_a_2025 = (
    'Palmeiras',         # 1º (Exemplo, verificar dados reais)
    'Flamengo',          # 2º
    'Red Bull Bragantino', # 3º
    'Cruzeiro',          # 4º
    'Fluminense',        # 5º
    'Ceará',             # 6º
    'Atlético-MG',       # 7º
    'Bahia',             # 8º
    'Botafogo',          # 9º
    'Corinthians',       # 10º
    'Fortaleza',         # 11º
    'Mirassol',          # 12º
    'Internacional',     # 13º
    'Vitória',           # 14º
    'Grêmio',            # 15º
    'São Paulo',         # 16º
    'Vasco da Gama',     # 17º
    'Juventude',         # 18º
    'Santos',            # 19º
    'Sport'              # 20º
)

print('-=' * 30)
print(f'{"CLASSIFICAÇÃO PARCIAL - BRASILEIRÃO SÉRIE A 2025":^60}')
print(f'{"(Atualizado em 15 de Maio de 2025)":^60}')
print('-=' * 30)

# a) Os 5 primeiros times
print(f'Os 5 primeiros times são: {tabela_brasileirao_serie_a_2025[0:5]}')
print('-=' * 30)

# b) Os últimos 4 colocados
print(f'Os últimos 4 colocados são: {tabela_brasileirao_serie_a_2025[-4:]}')
print('-=' * 30)

# c) Times em ordem alfabética
times_ordenados_serie_a_2025 = sorted(tabela_brasileirao_serie_a_2025)
print(f'Times em ordem alfabética: {times_ordenados_serie_a_2025}')
print('-=' * 30)

# d) Em que posição está o time da Chapecoense
time_procurado = 'Chapecoense'
if time_procurado in tabela_brasileirao_serie_a_2025:
    posicao_time_procurado = tabela_brasileirao_serie_a_2025.index(time_procurado) + 1
    print(f'A {time_procurado} está na {posicao_time_procurado}ª posição na Série A.')
else:
    # Verificar se a Chapecoense está na Série B, conforme dados anteriores
    tabela_brasileirao_serie_b_2025_exemplo = (
        'Goiás', 'Remo', 'Vila Nova', 'Avaí', 'Cuiabá',
        'CRB', 'Chapecoense', 'Coritiba', 'Athletico-PR', 'Operário-PR',
        'América Mineiro', 'Ferroviária', 'Atlético Goianiense', 'Novorizontino', 'Athletic',
        'Criciúma', 'Volta Redonda', 'Botafogo-SP', 'Paysandu', 'Amazonas'
    )
    if time_procurado in tabela_brasileirao_serie_b_2025_exemplo:
        posicao_chapecoense_serie_b = tabela_brasileirao_serie_b_2025_exemplo.index(time_procurado) + 1
        print(f'A {time_procurado} não está entre os 20 primeiros da Série A nesta data.')
        print(f'(Atualmente, a {time_procurado} consta na {posicao_chapecoense_serie_b}ª posição da Série B em 15/05/2025).')
    else:
        print(f'A {time_procurado} não foi encontrada na lista da Série A ou na lista de exemplo da Série B.')

print('-=' * 30)