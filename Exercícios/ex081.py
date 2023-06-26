repeat = 's'
num = []

while repeat == 's':
    n = int(input('Digite um valor: '))
    num.append(n)
    repeat = input('Quer continuar[S/N]? ').lower()


print('=-'*30)
print(f'Você digitou {len(num)} elementos')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {num}')

if 5 in num:
    print('O valor 5 faz parte da lista')

else:
    print('O valor 5 não faz parte da lista')