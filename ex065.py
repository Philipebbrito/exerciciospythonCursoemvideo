res = 'S'
n = soma = media = quant = menor = maior =  0
while res in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    res = str(input('QUER CONTINUAR? [S/N] ')).upper().strip()[0]
media = soma / quant
print(f'ACABOU!')
print(f'Voçê digitou {quant} números e a média foi {media:.2f}')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')