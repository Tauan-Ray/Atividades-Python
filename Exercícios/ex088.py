from random import randint
from time import sleep
numeros = []
pos = 1

print('-'*30)
print('     JOGA NA MEGA SENA       ')
print('-'*30)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=   SORTENDO {jogos} jogos -=-=-=')

for i in range(0, jogos):
    for i in range(0,6):
        n = randint(1,60)
        if n in numeros:
           n = randint(1,60)
           numeros.append(n)
        else:
            numeros.append(n)
            
    print(f'Jogo {pos}: {numeros}')
    sleep(1)
    pos+=1
    numeros.clear()

