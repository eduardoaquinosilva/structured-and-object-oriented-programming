def triangulo(x, soma):
    lista = []
    for a in range(1, x+1):
        lista.append(a)
        for b in lista:
            print(b, end=" ")
        print('')
        for i in lista:
            soma += i
    print(soma)


numero = int(input())
if numero > 0:
    triangulo(numero, 0)
elif numero == 0:
    print(0)
else:
    exit()
