pesos = []
pessoa = 1

for i in range(1, 6):
    pesop = float(input('Diga o peso da {}° pessoa: '.format(pessoa)))
    pessoa += 1
    pesos.append(pesop)

print('A pessoa com menor peso tem {} kilos'.format(min(pesos)))
print('A pessoa com maior peso tem {} kilos'.format(max(pesos)))
