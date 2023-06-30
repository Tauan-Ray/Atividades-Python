def contador(inicio, fim, passo):
    print('-='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo < 0:
        passo *= -1

    elif passo == 0:
        passo = 1

    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f'{cont}',end=' ')
            cont+=passo
        print('FIM')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}',end=' ')
            cont-= passo
        print('FIM')

contador(1,10,1)
contador(10,0,2)
print('-='*30)

print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)