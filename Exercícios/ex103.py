def ficha(jogador='<desconhecido>', gols=0):
    return f'O jogador {jogador} fez {gols} gol(s) no campeonato'


nome = str(input('Nome do Jogador: '))
gol = str(input('Número de Gols: '))

if gol.isnumeric():
    gol = int(gol)

else:
    gol = 0

if nome.strip() == '':
    print(ficha(gols=gol))

else:
    print(ficha(nome, gol))