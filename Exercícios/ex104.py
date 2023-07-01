def leiaInt(num):
    n = input(num)

    while n.isnumeric() == False:
        print('ERROR! Digite um número inteiro válido')
        n = input(num)

    if n.isnumeric():
        return n
    
num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}')