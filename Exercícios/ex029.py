vel = int(input('Digite a velocidade do carro: '))

if vel > 80:
    print("Você foi multado e deve pagar R${} ".format((vel-80)*7))

else:
    print('Você não foi multado')