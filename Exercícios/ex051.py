pt = int(input('Diga o primeiro termo: '))
r = int(input('Diga a razão: '))
decimo = pt+(10-1)*r

for i in range(pt, decimo, r):
    print(i)
    