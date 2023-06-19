somi = 0
nh = []
ih = []
contm = 0
contp = 1

for i in range(1, 5):
    print('----{}° pessoa----'.format(contp))
    nome = str(input('Diga o seu nome: '))
    idade = int(input('Diga a sua idade: '))
    sexo = str(input('Diga o seu sexo(M/F): ')).upper()
    if sexo == "M":
        nh.append(nome)
        ih.append(idade)
    
    elif sexo == "F":
        if idade < 20:
            contm+=1
    somi+=idade
    contp+=1

maxh = max(ih)
psi = ih.index(maxh)
nhv = nh[psi]

print("""A média de idade do grupo é {}
O nome do homem mais velho é {} tendo {} anos
Existem {} mulheres com menos de 20 anos""".format((somi/4), nhv, maxh, contm))


