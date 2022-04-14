tamanho = int(input())
if 0 > tamanho > 50 or tamanho % 2 != 0:
    exit()
vetor, parada, soma_jedi, soma_sith = [int(a) for a in input().split()], int(tamanho / 2), 0, 0
for b in vetor[:parada]:
    soma_jedi += b
for c in vetor[parada:]:
    soma_sith += c
if soma_jedi > soma_sith:
    print('Jedi')
elif soma_sith > soma_jedi:
    print('Sith')
else:
    print('Empate')
