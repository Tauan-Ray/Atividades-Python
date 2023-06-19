numeros = ('Zero','Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'Vinte')


user = int(input("Digite um número(Entre 0 e 20): "))

while user > 20 or user < 0:
    print('Tente novamente')
    user = int(input("Digite um número(Entre 0 e 20): "))

print(f'Você digitou o número {numeros[user]}')