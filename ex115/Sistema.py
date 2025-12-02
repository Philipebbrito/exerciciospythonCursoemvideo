from ex115.lib.interface import *
from ex115.lib.arquivo import *
import time

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['CADASTRAR USUÁRIO', 'LISTAR USUÁRIOS', 'SAIR DO SISTEMA'])
    if resp == 1:
        cabecalho('Opção 1')
        # Opção de cadastrar um novo usuário#
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 2:
        cabecalho('Opção 2')
        # Opção de listar o conteudo do arquivo#
        lerArquivo(arq)
    elif resp == 3:
        cabecalho('Saindo do Sistema ... Até Logo!')
        break
    else:
        print(f'\033[31mERRO! Digite uma opção válida!\033[m')
    time.sleep(2)