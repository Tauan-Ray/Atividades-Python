def dobro(m = 0):
    res = m * 2
    return res


def metade(m = 0):
    res = m / 2
    return res


def aumentar(m = 0, p = 0):
    res = m+(m*(p/100))
    return res


def diminuir(m = 0, p = 0):
    res = m-(m*(p/100))
    return res


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')