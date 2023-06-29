gol = list()
jogador = {'nome':'',
           'gols':gol}

jogador['nome'] = input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))

for i in range(0, partidas):
    gol.append(int(input(f'Quantos gols na partida {i}: ')))
    jogador['total'] = sum(gol)
print('=-'*30)

print(jogador)

print('=-'*30)

for k,v in jogador.items():
    print(f'O campo {k} tem o valor {v}')

print('=-'*30)

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')

for pos, i in enumerate(gol):
    print(f'=> Na partida {pos}, fez {i} gols.')
print(f'Foi um total de {sum(gol)} gols.')