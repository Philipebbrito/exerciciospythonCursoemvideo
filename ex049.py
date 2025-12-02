n = int(input('Digite um número para ver sua tabuada: '))
print('-' * 12)
for c in range(1, 11):
    print(f'{n} * {c:2} = {n*c:2}')
print('-' * 12)