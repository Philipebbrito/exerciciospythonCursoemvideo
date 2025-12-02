valor = float(input('Digite o valor do produto: R$'))
print('''FORMAS DE PAGAMENTO
[1] A vista DINHEIRO/CHEQUE
[2] A vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
pag = int(input('Qual a opção de pagamento: '))
if pag == 1:
    total = valor - (valor / 100 * 10)
    print(f'O valor om desconto é R${total:.2f}')
elif pag == 2:
    total = valor - (valor / 100 * 5)
    print(f'O valor com desconto é R${total:.2f}')
elif pag == 3:
    print('Dividindo em até 2x - PREÇO NORMAL!')
elif pag == 4:
    total = valor + (valor / 100 * 20)
    totparc = int(input('Quantas vezes: '))
    parcela = total / totparc
    print(f'Dividindo em {totparc}x, e com 20% de júros, o valor da parcela fica R${parcela:.2f}')
else:
    print('OPÇÃO INVÁLIDA!')
print(f'Sua compra no valor de R${valor:.2f} vai custar R${total:.2f}')