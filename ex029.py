velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80:
    print('-=-' * 20)
    print('MULTADO! Voçê excedeu o limite permitido que é de 80km/h')
    print('-=-' * 20)
    multa = (velocidade - 80) * 7
    print('Voçê deve pagar uma multa no valor de R${:.2f}'.format(multa))
print('Tenha um bom dia. Dirija com segurança!')