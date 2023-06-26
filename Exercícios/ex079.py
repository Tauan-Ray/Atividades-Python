repeat = 's'
num = []

while repeat == 's':
    n = int(input('Digite um valor: '))
    if n in num:
        print('Valor duplicado! Não vou adicionar...')
        repeat = input('Quer continuar[S/N]: ').lower()

    else:
        num.append(n) 
        print('Valor adicionado com sucesso...')
        repeat = input('Quer continuar[S/N]: ').lower()

num.sort()
print(f'Você digitou os valores {num}')

