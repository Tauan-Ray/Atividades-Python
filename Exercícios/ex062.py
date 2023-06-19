pt = int(input('Diga o valor primeiro termo: '))
r = int(input('Diga o valor da razão: '))
termo = pt
cont = 1

while cont <=10:
    print(f'{termo} /', end='')
    termo = termo + r
    cont+=1

paro = 0

while paro == 0:
    op = int(input('\nQuantos termos você quer mostras a mais? '))
    if op != 0:
        cont-=op
        while cont <= 10:
            print(f'{termo} /', end='')
            termo = termo + r
            cont+=1
    
    else:
        paro+=1
