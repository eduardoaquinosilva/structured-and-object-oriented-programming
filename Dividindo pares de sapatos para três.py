a, b = int(input()), int(input())
soma = 0
if a > b:
    print('invalido')
else:
    for i in range(a, b+1):
        if i % 2 == 0 and i % 3 == 0:
            soma += i
    print(soma)
