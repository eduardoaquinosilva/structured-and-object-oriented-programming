from math import pow, sqrt


def distancia(x, y):
    d = sqrt(pow(x, 2) + pow(y, 2))
    if d < 0:
        d *= -1
    else:
        print(f'{d:.2f}')


x1, y1 = [int(a) for a in input().split()]
x2, y2 = [int(b) for b in input().split()]
x, y = x2 - x1, y2 - y1
distancia(x, y)
