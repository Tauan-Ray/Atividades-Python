def leiaInt(num):
    while True:
        try:
            n = int(input(num))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido.')
            continue
        except KeyboardInterrupt():
            print('Entrada de dados interrompida pelo usuário')
        else:
            return n
        

def linha(tam = 42):
    return '-' * 42


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\33[32mSua opção: \33[m')
    return opc