repeat = 'S'
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

while repeat == 'S':
    print('''----Opções----
    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa\n''')

    op = int(input('Escolha uma opção: '))

    if op == 1:
        print(f'{n1} + {n2} = {n1+n2}')
    
    elif op == 2:
        print(f'{n1} * {n2} = {n1*n2}')
    
    elif op == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        
        else:
            print(f'O maior número é {n2}')
        
    elif op == 4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    
    elif op == 5:
        repeat = 'N'
        print('Programa finalizado')
        exit()
    

    repeat = str(input(f'Você deseja usar o programa denovo[S/N]? ')).upper()

    