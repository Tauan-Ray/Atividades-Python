cont = 1

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    cont= 0 
    while cont <=10:
        print(f'{n} * {cont} = {n*cont}')
        cont+=1
    