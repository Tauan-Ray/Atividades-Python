#valor da casa
#salario do comprador
#Em quantos anos ele vai pagar
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valc = float(input('Informe o valor da casa: '))
sal = float(input('Informe o seu salário: '))
qtda = int(input('Informe em quantos anos você vai pagar a casa: '))

sal30 = sal*0.30
prestacao = valc/(qtda*12)

if prestacao > sal30:
    print('Infelizmente seu empréstimo foi negado por conta de seu salário')

else:
    print('Seu empréstimo foi aprovado')