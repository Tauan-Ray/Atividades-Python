from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'Exercícios/ex115/cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


cabeçalho('SISTEMA ARQUIVO v1.0')

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoaa', 'Sair do Sistema'])
    if resp == 1:
        # Opção de listar o conteudo de um arquivo
        lerArquivo(arq)

    elif resp == 2:
        # Opção cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)

    elif resp == 3:
        # Opção de sair do programa
        cabeçalho('Saindo do programa... Até logo')
        break

    else:
        print('\33[31mERRO! Digite uma opção válida\33[m')
    sleep(2)

