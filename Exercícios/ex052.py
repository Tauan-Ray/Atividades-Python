n = int(input('Diga um número inteiro: '))
cont = 0

for i in range(1, n+1):
    if n % i == 0:
        print('\033[33m', end=' ')
        cont += 1

    else:
        print('\033[31m', end=' ')
    
    print(i, end = '')

print('\n\033[mO número {} foi divisivel {} vezes'.format(n, cont))

if cont == 2:
    print('Por isso ele é primo')

else:
    print('Por isso ele não é primo')