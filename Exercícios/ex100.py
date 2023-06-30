from random import randint

numeros = list()

def sorteia():
    print('Sorteando 5 valores da lista ',end='')
    for i in range(0,5):
        numeros.append(randint(1,10))
    for v in numeros:
        print(v,end=' ')
    print('PRONTO')

def somaPar():
    sum = 0
    for v in numeros:
        if v % 2 == 0:
            sum+= v
    print(f'Somandos os valores pares de {numeros}, temos {sum}')

sorteia()
somaPar()