from random import randint

pc = randint(1, 10)
user = int(input('Escolha um número: '))
palp = 1

while user != pc:
    user = int(input('Você escolheu o número errado. Escolha outro número: '))
    palp+=1

print(f'Parabéns você acertou o número em {palp} tentativas')

    