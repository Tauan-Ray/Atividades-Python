from datetime import date

anoat = date.today().year
ano = int(input('Informe seu ano de nascimento: '))
idd = anoat-ano

if idd > 0 and idd <=9:
    print('Mirin')

elif idd > 9 and idd <=14:
    print('Infantil')

elif idd > 14 and idd <= 19:
    print('Júnior')

elif idd > 19 and idd <= 25:
    print('Sênior')

else:
    print('Master')