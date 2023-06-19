produtos = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25)

print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*50)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')

    else:
        print(f'R${produtos[pos]:>7.2f}')

print('-'*60)