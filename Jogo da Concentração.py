a, b = [int(i) for i in input().split()]
if b < a:
    exit()
resultado_final, cont, lista1, lista2 = [], 0, [c for c in list(range(a, b+1))], [d for d in list(range(b, a-1, -1))]
for e in range(len(lista1)):
    resultado_final.append(lista1[e])
    resultado_final.append(lista2[e])
print(resultado_final)
