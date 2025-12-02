valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))

maior = max(valores)
menor = min(valores)

print('=-'*25)
print(f'Voçê digitou os valores {valores}')
print(f'O maior valor digitado foi {maior}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor}, nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')