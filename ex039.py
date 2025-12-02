nasc = int(input('Ano de nascimento: '))
idade = 2025 - nasc
print(f'No ano de 2025 voçê completa {idade} anos!')
if idade == 18:
    print('Este é o ano exato para o seu alistamento militar!')
elif idade < 18:
    print('Ainda não chegou a o momento para o seu alistamento militar')
    print(f'Ainda faltam {18 - idade} anos!')
    print(f'Seu alistamento será em {nasc + 18}')
elif idade > 18:
    print('Voçê já passou do periodo obrigatório para o alistamento!')
    print(f'Seu alistamento foi em {nasc + 18}')
    print(f'Voçê já deveria ter se alistado a {idade - 18} anos!')