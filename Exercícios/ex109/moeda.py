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