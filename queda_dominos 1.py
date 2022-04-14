n = int(input())
if 0 > n > 50:
    exit()
dominos = [int(a) for a in input().split()]
print('ok' if dominos == sorted(dominos) else 'precisa de ajuste')
