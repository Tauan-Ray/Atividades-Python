from random import choice

e = int(input('Escolha um número de 0 a 5: '))

pc = choice([0, 5])

if e == pc:
    print('Você ganhou')
else:
    print('Você perdeu')
