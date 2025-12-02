larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensao de {}mt X {}mt e sua área é de {}mt²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede voce vai precisar de {}lts de tinta'.format(tinta))