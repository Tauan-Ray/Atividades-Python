s = float(input('Diga o seu salário: '))

if s > 1250:
    print('O seu novo salário é de {}'.format(s+(s*(10/100))))

else:
    print('O seu novo salário é de {}'.format(s + (s * (15 / 100))))
