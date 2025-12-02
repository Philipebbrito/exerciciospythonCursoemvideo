nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'Primira nota {nota1} e Segunda nota {nota2}, sua média é {media:.2f}')
if media < 5.0:
    print('REPROVADO')
elif media == 5.0 or media <= 6.9:
    print('RECUPERAÇÃO')
elif media > 7.0:
    print('APROVADO')