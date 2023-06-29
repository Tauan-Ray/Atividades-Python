aluno = dict()

nome = input('Nome: ')
media = float(input(f'Média de {nome}: '))

if media >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

aluno['nome'] = nome
aluno['media'] = media
aluno['situacao'] = situacao

for k,v in aluno.items():
    print(f'O {k} é igual a {v}')
