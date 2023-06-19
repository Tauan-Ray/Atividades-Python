from random import randint


print('''Escolha uma opção
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
op = int(input('Escolha uma opção: '))

pcesco = randint(0, 2)

if op == 0 and pcesco == 1:
    print(' O pc jogou {} você perdeu'.format(pcesco))

elif op == 1 and pcesco == 2:
    print(' O pc jogou {} você perdeu'.format(pcesco))

elif op == 2 and pcesco == 0:
    print(' O pc jogou {} você perdeu'.format(pcesco))

elif op == pcesco:
    print('Empate')

else:
    print('O pc jogou {} você ganhou'.format(pcesco))