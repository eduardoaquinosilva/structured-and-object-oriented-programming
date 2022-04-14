quant_conj_cartas = [int(i) for i in input().split()]
quantidade, conjunto_cartas, soma, cont = quant_conj_cartas[0], quant_conj_cartas[1:], 0, 0
for a in conjunto_cartas:
    if a == 1:
        soma += 11
        cont += 1
    elif 10 >= a >= 2:
        soma += a
    elif a == 11 or a == 12 or a == 13:
        soma += 10
while cont > 0:
    if soma <= 21:
        break
    else:
        soma -= 10
        cont -= 1
print(soma)
