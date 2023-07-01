def notas(*notas, sit=False):
    ficha = dict()
    ficha['total'] = len(notas)
    ficha['maior'] = max(notas)
    ficha['menor'] = min(notas)
    ficha['média'] = sum(notas)/len(notas)
    if sit:
        if ficha['média'] >= 7:
            ficha['situação'] = 'BOA'

        elif ficha['média'] >= 5:
            ficha['situação'] = 'RAZOÁVEL'

        else:
            ficha['situação'] = 'RUIM'

    return ficha            

resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)