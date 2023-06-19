ano = int(input('Informe o seu ano de nascimento: '))

idade = 2023-ano

if idade < 18:
    print('''Você possui {} e ainda vai se alistar ao serviço militar. Faltam {} anos para você poder se alistar'''
          .format(idade, 18-idade))

elif idade == 18:
    print('É a hora exata de se alistar')

else:
    print('''Você possui {} anos e ja deveria ter se alistado. Seu alistamento deveria ter sido feito a {} anos atrás'''
          .format(idade, idade-18)) 