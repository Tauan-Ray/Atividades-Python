maiorida = 0
conth = 0
idadm = 0

while True:
    idade = int(input('Informe a sua idade: '))
    sexo = str(input('Informe o seu sexo [M/F]: ')).upper()

    if idade > 18:
        maiorida+=1
    
    elif sexo == 'M':
        conth+=1
    
    elif sexo == 'F':
        if idade < 20:
            idadm+=1
    
    conti = str(input('Você quer continuar? [S/N]')).upper()
    if conti == 'N':
        break

print(f'''{maiorida} pessoas tem mais de 18 anos
{conth} homens foram registrados
{idadm} mulheres tem menos de 20 anos''')
