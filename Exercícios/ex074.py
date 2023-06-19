import random

numeros_aleatorios = tuple(random.sample(range(1, 100), 5))
print(f'Os valores sorteados foram: {numeros_aleatorios}')
print(f'O maior valor sorteado foi {max(numeros_aleatorios)}')
print(f'O menor valor sorteado foi {min(numeros_aleatorios)}')