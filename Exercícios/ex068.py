from random import randint
soma = 0
vit = 0


while True:
    pc = randint(1, 10)
    user = int(input('Digite um valor: '))
    esco = str(input('Par ou ímpar? [P/I] ')).upper()
    soma = user + pc
    if esco == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {user} e o pc {pc}. Total deu {soma} deu par')
            print('Você ganhou parabéns')
            vit+=1

        elif soma % 2 != 0:
            print(f'Você jogou {user} e o pc {pc}. Total deu {soma} deu impar')
            print('Você perdeu')
            break

    elif esco == 'I':
        if soma % 2 !=0:
            print(f'Você jogou {user} e o pc {pc}. Total deu {soma} deu impar')
            print('Você ganhou parabéns')
            vit+=1

        elif soma % 2 == 0:
            print(f'Você jogou {user} e o pc {pc}. Total deu {soma} deu par')
            print('Você perdeu')
            break

print(f'GAME OVER! Você venceu {vit} vezes')
    
