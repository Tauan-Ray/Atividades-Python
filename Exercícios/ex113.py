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
        
def leiaFloat(num):
    while True:
        try:
            n = float(input(num))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número real válido.')
            continue
        except KeyboardInterrupt():
            print('Entrada de dados interrompida pelo usuário')
            return 0
        else:
            return n
 


inteiro = leiaInt('Digite um número inteiro: ')
real = leiaFloat('Digite um número Real: ')

print(f'O valor inteiro digitado foi {inteiro} e o número real foi {real}')