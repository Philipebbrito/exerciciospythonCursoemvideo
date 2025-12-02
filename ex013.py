salario = float(input('Qual o salário do funcionário: R$'))
novo = salario + (salario * 5 / 100)
print('O salário que era R${:.2f}, com o aumento de 5% passa a receber R${:.2f}'.format(salario,novo))