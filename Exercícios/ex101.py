from datetime import datetime

def voto(nasc):
    global idade
    idade = datetime.now().year - nasc
    if idade < 18:
        return f'Com {idade}: VOTO NEGADO'
    
    elif idade >= 18 and idade < 65:
        return f'Com {idade}:VOTO OBRIGATÓRIO'

    elif idade >= 65:
        return f'Com {idade}: VOTO OPCIONAL'

ano = int(input('Em que ano você nasceu? '))
print(voto(ano))