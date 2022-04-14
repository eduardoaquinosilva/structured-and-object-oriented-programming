quant_pessoas, pessoas, professores, alunos = int(input()), [int(a) for a in input().split()], [], []
for b in pessoas:
    if b % 2 == 0:
        professores.append(b)
    else:
        alunos.append(b)
print('[', end=" ")
for c in alunos:
    print(c, end=" ")
print(']')
print('[', end=" ")
for d in professores:
    print(d, end=" ")
print(']')
