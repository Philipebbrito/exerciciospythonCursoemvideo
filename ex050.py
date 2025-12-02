p = 0
cont = 0
for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
       p = p + n
       cont = cont + 1
print(f'O resultado dos {cont} números pares é {p}')