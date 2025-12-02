n = c = soma = 0
while True:
    n = int(input('Digite um número [DIGITE 999 PARA PARAR]: '))
    if n == 999:
        break
    c += 1
    soma += n
print(f'{c} números digitados e a soma deles é {soma}')