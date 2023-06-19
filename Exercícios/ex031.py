d = float(input('Digite a distância da viagem em Km: '))

if d <= 200:
    print('O custo da passagem é de R${}'.format(d*0.50))

else:
    print('O custo da passagem é de R${}'.format(d * 0.45))
