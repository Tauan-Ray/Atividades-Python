acumula = 0
cont =0

for i in range(1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
           cont += 1
           acumula += i

print('A soma dos {} valores é {}'.format(cont, acumula))
 