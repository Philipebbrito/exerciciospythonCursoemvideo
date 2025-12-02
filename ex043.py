peso = float(input('Digite seu peso: KG'))
alt = float(input('Digite sua altura: M'))
imc = peso / (alt ** 2)
print(f'O seu imc é de {imc:.1f}')
if imc < 18.5:
    print('IMC ABAIXO DO PESO!')
elif imc <= 25:
    print('PESO IDEAL!')
elif imc <= 30:
    print('SOBREPESO!')
elif imc <= 40:
    print('OBESIDADE!')
elif imc > 40:
    print('OBESIDADE MORBIDA!')
else:
    print('TENTE NOVAMENTE!!!')