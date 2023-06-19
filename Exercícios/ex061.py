pt = int(input('Diga o valor primeiro termo: '))
r = int(input('Diga o valor da razão: '))
termo = pt
cont = 1

while cont <=10:
    print(f'{termo} /', end='')
    termo = termo + r
    cont+=1
print('Fim')