frase = str(input('Diga uma frase: ')).strip().upper()

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for i in range(len(junto)-1, -1, -1):
    inverso += junto[i]

if inverso == junto:
    print('A frase é um palindromo')

else:
    print('A frase não é um palindromo')