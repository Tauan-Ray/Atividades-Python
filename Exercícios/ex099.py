def maior(*num):
    cont = maior = 0 
    print('=-'*30)
    print('Analisando os valores passados...')
    for i in num:
        print(i,end=' ')
        if cont == 0:
            maior = i
        else:
            if i > maior:
                maior = i
        cont+=1
    print(f'Foram informado {cont} valores ao todo')
    print(f'O maior valor informado foi {maior}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()