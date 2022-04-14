quant_vetor = int(input())
if quant_vetor > 50:
    exit()
vetor, cont1, cont2 = [int(a) for a in input().split()], 0, 0
for b in vetor:
    if b >= 0:
        cont1 += 1
    else:
        cont2 += 1
if cont1 > cont2:
    semi_final = cont1 - cont2
    final = cont1 - semi_final
elif cont1 == cont2:
    final = cont1
else:
    semi_final = cont2 - cont1
    final = cont2 - semi_final
print(final)
