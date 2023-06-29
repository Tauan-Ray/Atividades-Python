dados = dict()
pessoas = list()
sumId = 0 

repeat = 's'

while repeat == 's':
    dados['nome'] = input('Nome: ')
    dados['sexo'] = input('Sexo: [M/F] ').lower()
    while dados['sexo'] != 'm' and dados['sexo'] != 'f':
        print('ERRO! Por favor digite apenas M ou F')
        dados['sexo'] = input('Sexo: [M/F] ').lower()

    dados['idade'] = int(input('Idade: '))
    sumId+=dados['idade']
    pessoas.append(dados.copy())
    repeat = input('Quer continuar? [S/N]').lower()

    while repeat != 's' and repeat != 'n':
        print('ERRO! Responda apenas com S ou N')
        repeat = input('Quer continuar? [S/N]').lower()

print('=-'*30)
media = sumId/len(pessoas)

print(f'Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f'A média de idade é de {media}')
print('As mulheres cadastradas foram: ',end='')
for p in pessoas:
    if p['sexo'] == 'f':
        print(f'{p["nome"]}', end=' ')

print()

print('Lista das pessoas que estão acima da média: ',end='')
for p in pessoas:
    if p['idade'] >= media:
        print('     ')
        for k,v in p.items():
            print(f'{k} = {v}; ',end='')
        print()

print('ENCERRADO')
