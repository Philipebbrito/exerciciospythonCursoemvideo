def escreva(texto):
    tamanho = len(texto) + 8
    print('~' * tamanho)
    print(f'    {texto}')
    print('~' * tamanho)


while True:
    txt = str(input('Digiteum texto: '))
    escreva(txt)