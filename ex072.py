cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
        'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', ' Catorze', 'Quinze',
        'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    while True:
        try:
            numero = int(input('Digite um número entre 0 e 20: '))
            if 0 <= numero <= 20:
                break
            else:
                print('Número inválido. Por favor, digite um número entre 0 e 20.')
        except ValueError:
            print('Entrada inválida. Por favor, digite um número inteiro.')

    print(f'Você digitou o número: {cont[numero]}')

    continuar = input('Deseja digitar outro número? (S/N): ').strip().upper()
    if continuar != 'S':
        break

print('Programa encerrado.')


