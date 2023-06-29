pessoas = list()
dados = list()
repeat = 's'
maiorP = menorP = 0

while repeat == 's':
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(pessoas) == 0:
        maiorP = menorP = dados[1]
    else:
        if dados[1] > maiorP:
            maiorP = dados[1]
        if dados[1] < menorP:
            menorP = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    repeat = input('Quer continuar[S/N]? ').lower()

print('=-'*30)
print(f'Você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi de {maiorP} Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorP:
        print(f'{p[0]}', end='... ')
print()
print(f'O menor peso foi de {menorP}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorP:
        print(f'{p[0]}', end='... ')
