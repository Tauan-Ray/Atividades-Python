def ajuda(com):
    título(f'Acessando manual do comando {com}')
    help(com)

def título(msg):
    tamanho = len(msg) + 4
    print('~'*tamanho)
    print(f'  {msg}')
    print('~'*tamanho)

comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

título('ATÉ LOGO',)
