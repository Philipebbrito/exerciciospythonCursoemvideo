frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

'''inverso = '''''
'''for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]'''
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')

if inverso == junto:
    print('PALINDROMO')
else:
    print('NAO PALINDROMO')