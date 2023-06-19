times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco da Gama', 'Chapecoense', 'Atlético-MG', 'Botafogo',
         'Athletico-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atléico-GO')

print('Lista de times do Brasileirão: ', times)
print('Os cinco primeiro são ',times[0:5])
print('Os 4 últimos são ',times[-4:])
print('Times em ordem alfabética: ',sorted(times))
pos = times.index('Chapecoense')
print(f'O Chapecoense está na {pos+1}º posição')