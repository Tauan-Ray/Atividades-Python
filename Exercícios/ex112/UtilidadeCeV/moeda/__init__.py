def dobro(m = 0, formato=False):
    res = m * 2
    return res  if formato is False else moeda(res)

def metade(m = 0, formato = False):
    res = m / 2
    return res if formato is False else moeda(res)


def aumentar(m = 0, p = 0, formato = False):
    res = m+(m*(p/100))
    return res if formato is False else moeda(res)


def diminuir(m = 0, p = 0, formato = False):
    res = m-(m*(p/100))
    return res if formato is False else moeda(res)


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')

def resumo(m= 0 ,a= 10 ,r = 5):
    print('-'*30)
    print('       RESUMO DO VALOR     ')
    print('-'*30)

    print(f'Preço analisado:    {moeda(m)}')
    print(f'Dobro do preço:     {dobro(m, True)}')
    print(f'Metade do preço:    {metade(m, True)}')
    print(f'{a}% de aumento:    {aumentar(m,a,True)}')
    print(f'{r}% de redução:    {diminuir(m,r,True)}')

    print('-'*30)