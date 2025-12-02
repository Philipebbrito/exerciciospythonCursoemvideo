'''Exercício Python 110: Adicione o módulo moeda.py
criado nos desafios anteriores, uma função chamada
resumo(), que mostre na tela algumas informações geradas
pelas funções que já temos no módulo criado até aqui.'''

import moeda110

valor = float(input('Digite um valor em R$ '))
aumento = int(input('Aumento: '))
desconto = int(input('Desconto: '))


print(moeda110.resumo(valor,aumento,desconto))