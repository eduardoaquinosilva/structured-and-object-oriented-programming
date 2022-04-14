quant = int(input())
if quant == 0:
    print('[]')
else:
    cartas = [int(a) for a in input().split()]
    for b in cartas:
        if b == 1:
            cartas.insert(cartas.index(b), 'A')
            cartas.remove(b)
        elif b == 11:
            cartas.insert(cartas.index(b), 'J')
            cartas.remove(b)
        elif b == 12:
            cartas.insert(cartas.index(b), 'Q')
            cartas.remove(b)
        elif b == 13:
            cartas.insert(cartas.index(b), 'K')
            cartas.remove(b)
    print(cartas)
