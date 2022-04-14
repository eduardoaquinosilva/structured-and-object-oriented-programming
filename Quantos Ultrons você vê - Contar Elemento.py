ultron, total_elementos = [int(i) for i in input().split()]
if 0 > ultron > 9 or 1 > total_elementos > 50:
    exit()
vetor = [int(a) for a in input().split()]
print(vetor.count(ultron))
