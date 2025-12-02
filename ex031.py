distancia = float(input('Qual é a distancia da sua viagem? '))
print('Voçê está prestes a iniciar uma viagem de {}km.'.format(distancia))
'''if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45'''
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))