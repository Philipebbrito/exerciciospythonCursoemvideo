real = float(input('Qual o seu saldo: R$'))
dolar = real / 5.792
euro = real / 6.04
print('Com R${} voçê tem U${:.2f} e Euro${:.2f}'.format(real,dolar, euro))