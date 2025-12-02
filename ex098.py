from time import sleep

def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    print('~~'*30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' => ')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' => ')
            sleep(0.5)
            cont -= p
        print('FIM!')


#programa prncipal
while True:
    inicio = int(input('Inicio: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('-='*30)
    contador(inicio, fim, passo)
    print('-='*30)
    res = str(input('Deseja continuar?: [S/N]')).strip().upper()[0]
    if res in 'N':
        break

print('~'*30)
print('CONTADOR ENCERRADO!!!')
print('~'*30)