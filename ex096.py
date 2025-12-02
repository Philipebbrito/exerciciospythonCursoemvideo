def area(largura, comprimento):
    res = largura * comprimento
    print(f'A área de um terreno {largura}m x {comprimento}m é de {res} m2')


print('-'*30)
print(f'{'     Controle de Terreno     '}')
print('-'*30)
larg = float(input('LARGURA(m): '))
comp = float(input('COMPRIMENTO(m): '))
area(larg, comp)