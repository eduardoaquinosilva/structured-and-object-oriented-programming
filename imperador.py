import numpy as np
lc, soma_c, soma_g = int(input()), 0, 0
matriz = list(np.zeros((lc, lc), dtype=str))
for a in range(lc):
    matriz[a] = input().split()
for b in matriz:
    cont = 0
    for c in b:
        if 'L' in b:
            break
        if c == 'C':
            if cont == (lc - (matriz.index(b) + 1)):
                soma_c += 2
            else:
                soma_c += 1
        elif c == 'G':
            soma_g += 2
        else:
            exit()
        cont += 1
if soma_c > soma_g:
    print('Condenados a morte')
elif soma_c < soma_g:
    print('Gladiadores')
else:
    print('Ninguém')
