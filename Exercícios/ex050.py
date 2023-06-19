acumula = 0
cont = 1

for i in range(1, 7):
    n = int(input("Digite o {} valor: ".format(cont)))
    cont+=1
    if n % 2 == 0:
        acumula += n

print('A soma de todos os números pares ditos é {}'.format(acumula))