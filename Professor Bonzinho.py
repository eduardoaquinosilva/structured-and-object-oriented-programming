lista = []
p1, p2, p3, t  = float(input()), float(input()), float(input()), float(input())
lista.append(p1); lista.append(p2); lista.append(p3); lista.sort(); lista.pop(0)
n1, n2 = float(lista[0]), float(lista[1])
media = (n1 + n2 + t) / 3
if media >= 7:
    print(f'Aprovado com {media:.1f}')
else:
    print(f'Final com {media:.1f}')
