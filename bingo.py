matriz, vetor = (1, 9, 27, 23, 34, 20, 37, 47, 30, 87, 55, 69, 13, 60, 99, 66), [int(i) for i in input().split()]
cont = 0
if len(vetor) > 6:
    exit()
for a in matriz:
    for b in vetor:
        if a == b:
            cont += 1
print(cont)
