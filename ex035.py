print('-=-' * 20)
print('Analisando Triangulos')
print('-=-' * 20)
r1 = float(input('reta 01: '))
r2 = float(input('reta 02: '))
r3 = float(input('reta 03: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima podem formar triangulo!!!')
else:
    print('Os seguimentos acima NÃO podem formar triangulo!!!')