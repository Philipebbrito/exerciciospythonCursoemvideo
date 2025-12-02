r1 = int(input('Primeiro Segmento: '))
r2 = int(input('Segundo Segmento: '))
r3 = int(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar um triangulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISOCELES!')
else:
    print('NÃO PODEM FORMAR TRIANGULO')
