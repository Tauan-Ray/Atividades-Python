soma = 0
contn = 0

n = int(input('Digite um número: '))
soma+=n
contn+=1

while n != 999:

    n = int(input('Digite um número: '))
    soma+=n
    contn+=1

print(f'Você digitou {contn-1} e a soma entre eles foi {soma-999}')