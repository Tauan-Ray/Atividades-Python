prod = float(input('Informe o preço do produto: '))

print('''Escolha o método de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Escolha uma opção: '))

if op == 1:
    pf = prod-(prod*(10/100))
    print('Escolhendo pagar à vista dinheiro/cheque você recebe 10% de desconto, pague apenas R${}'.format(pf))

elif op == 2:
    pf = prod-(prod*(5/100))
    print('Escolhendo pagar à vista no cartão você recebe 5% de desconto, pague apenas R${}'.format(pf))

elif op == 3:
    print('Você escolheu pagar em até 2x no cartão, e não recebe descontos, pague R${}'.format(prod))

else:
    pf = prod+(prod*(20/100))
    print('Escolhendo pagar 3x ou mais no cartão você sera cobrado com mais 20% de juros, pague no total R${}'.format(pf))
