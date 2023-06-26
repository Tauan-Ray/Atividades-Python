repeat = 's'
num = []
impar = []
par = []

while repeat == 's':
    n = int(input('Digite um número: '))
    num.append(n)
    if n % 2 == 0:
        par.append(n)
    else: 
        impar.append(n)
    repeat = input('Quer continuar[S/N]? ').lower()

print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
