matriz, d_princ, d_sec, cont = [[], [], [], [], []], 0, 0, 0
for a in range(5):
    matriz[a] = [int(b) for b in input().split()]
for c in range(5):
    d_princ += matriz[c][c]
for d in range(-1, -6, -1):
    d_sec += matriz[cont][d]
    cont += 1
print(d_princ - d_sec)
