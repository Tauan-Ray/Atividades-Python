valores = []
pos = 0

for i in range(1, 6):
    num = int(input(f'Digite um valor para a posição {pos}: '))
    valores.append(num)
    pos+=1

maior = max(valores)
menor = min(valores)
print('=-'*20)

print(f'Você digitou os valores {valores}')
print(f'O maior valor foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end='')
print()
    
print(f'O menor valor foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}... ', end='')