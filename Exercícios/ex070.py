soma = 0 
produc = 0
precob = []
nprecob = []

while True:
    nome = str(input('Informe o nome do produto: '))
    preco = float(input('Informe o preço do produto: '))
    nprecob.append(nome)
    precob.append(preco)

    soma+=preco
    
    if preco > 1000:
        produc+=1

    conti = str(input('Você quer continuar?[S/N] ')).upper()
    if conti == 'N':
        break


cheap = min(precob)
psb = precob.index(cheap)
npb = nprecob[psb]

print(f'''Você gastou R${soma} nas suas compras
{produc} produtos custam mais de R$1000
{npb} é o produto mais barato''')
