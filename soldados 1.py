quant_solds, solds, soma = int(input()), [float(i) for i in input().split()], 0
for a in solds:
    soma += a
media = soma / quant_solds
print(f'{media:.2f}')
for b in solds:
    if b < media:
        print('P', end=" ")
    elif b == media:
        print('M', end=" ")
    else:
        print('G', end=" ")
