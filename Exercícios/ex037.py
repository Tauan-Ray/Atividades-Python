n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para a conversão')

print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')
opc = int(input('Escolha uma opção: '))

if opc == 1:
    print('{} convertido para binário é igual a {}'.format(n, bin(n)[2:]))

elif opc == 2:
   print('{} convertido para octal é igual a {}'.format(n, oct(n)[2:]))

elif opc == 3:
     print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)[2:]))

else:
    print('Opção inválida')