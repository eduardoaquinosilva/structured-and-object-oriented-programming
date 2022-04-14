casos, lista = int(input()), []
for a in range(casos):
    tamanho, grito = [int(b) for b in input().split()]
    if tamanho >= 100 or 0 > grito > 100:
        exit()
    operarios = [int(c) for c in input().split()]
    for d in operarios:
        if d == grito:
            if operarios.index(d) != 0 and operarios.index(d) != tamanho - 1:
                operarios[operarios.index(d) - 1] *= -1
                operarios[operarios.index(d) + 1] *= -1
            elif operarios.index(d) == 0:
                operarios[operarios.index(d) + 1] *= -1
            else:
                operarios[operarios.index(d) - 1] *= -1
    lista.append(operarios)
for e in lista:
    print(e)
