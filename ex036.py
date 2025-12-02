valorcs = float(input('Digite o valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Em quantos anos vc vai financiar: '))
prestacao = valorcs / (anos * 12)
limite = salario * 30 / 100
print(f'Para comprar uma casa de R${valorcs:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}.')
if prestacao <= limite:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo negado!')