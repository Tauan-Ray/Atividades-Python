from datetime import date

atual = date.today().year
acumula = 0 
pessoa = 1

for i in range(1, 8):
    ano = int (input('Diga em que ano a {}° pessoa nasceu: '.format(pessoa)))
    pessoa+=1
    idade = atual - ano
    if idade < 18:
        acumula+=1

print('{} pessoas ainda não atingiram a maioridade'.format(acumula))
print('{} pessoas já atingiram a maioridade'.format(7-acumula))