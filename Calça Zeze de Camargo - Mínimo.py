lista = []
for i in range(5):
    n = int(input())
    if 0 > n > 30:
        print('Número deve estar entre 1 e 30')
        exit()
    else:
        lista.append(n)
print(min(lista))
