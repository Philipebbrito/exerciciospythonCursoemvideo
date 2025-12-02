from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opcao = int(input('>>>>>>> QUAL SUA OPÇÃO???: '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma de {n1} + {n2} é igual a {soma}')
    elif opcao ==2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é igual a {produto}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'O maior número digitado foi {maior}')
    elif opcao == 4:
        print('INFORME OS NUMEROS NOVAMENTE')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('FINALIZANDO')
    else:
        print('OPÇÃO INVALIDA!!!')
    sleep(2)
print('FIM DO PROGRAMA!!!')
