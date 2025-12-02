salario = float(input('Qual o seu salário? '))
if salario > 1250:
    novo = salario + (salario / 100) * 10
    print('Seu salário de R${:.2f}, com aumento de 10% vai para R${:.2f}'.format(salario, novo))
else:
    novo = salario + (salario / 100) * 15
    print('Seu salário de R${:.2f}, com aumento de 15% vai para R${:.2f}'.format(salario, novo))