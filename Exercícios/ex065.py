paro = 0
soma =  0
cont = 0
l = []

while paro == 0:
    n = int(input('Digite um número: '))
    l.append(n)
    soma+=n
    cont+=1
    op = str(input('Quer continuar? [S/N] ')).upper()
    if op == 'N':
        paro+=1

media = soma/cont
print(f'Você digitou {cont} números  e a média foi {media}')
print(f'O maior valor foi {max(l)} e o menor foi {min(l)}')



