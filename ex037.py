numero = int(input('Digite um número inteiro: '))
print('[1] Converter para Binário')
print('[2] Converter para Octal')
print('[3] Converter para Hexadecimal')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{numero} convertido para Binário é {bin(numero)[2:]}')
elif opcao == 2:
    print(f'{numero} convertido para Octal é {oct(numero)[2:]}')
elif opcao == 3:
    print(f'{numero} convetido para Hexadecimal é {hex(numero)[2:]}')
else:
    print('Opção inválida!!!')
    print('TENTE NOVAMENTE!!!')