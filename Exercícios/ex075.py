n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

tupla_numeros = (n1, n2, n3, n4)
print(f'Você digitou os valores {tupla_numeros}')
print(f'O valor 9 apareceu {tupla_numeros.count(9)} vezes')
if 3 in tupla_numeros:
    print(f'O valor 3 apareceu na {tupla_numeros.index(3)+1}º posição')

else:
    print('O valor 3 não foi digitado em nenhuma posição')

print(f'Os valores pares digitados foram ', end='')

for n in tupla_numeros:
    if n % 2 == 0:
        print(n, end=' ')      


