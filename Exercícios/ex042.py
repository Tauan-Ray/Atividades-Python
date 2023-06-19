l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 == l3:
        print('Os segmentos acima podem formar um triângulo equilátero')
    
    elif l1 != l2 != l3 != l1:
        print('Os segmentos acima podem formar um triângulo escaleno')

    else:
        print('Os segmentos acima podem formar um triângulo isósceles')

else:
    print('Os segmentos não podem formar um triângulo')
