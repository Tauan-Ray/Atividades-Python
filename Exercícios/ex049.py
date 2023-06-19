n = int(input("Diga o número que você quer a tabuada: "))

for i in range(1, 11):
    print('{} * {} = {}'.format(n, i, n*i))