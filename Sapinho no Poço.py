p, s, e = int(input()), int(input()), int(input())
if s > p:
    exit()
caminho = s
print(0, caminho)
while caminho < p:
    caminho -= e
    print(caminho, end=" ")
    caminho += s
    if caminho < p:
        print(caminho)
    else:
        print('saiu')
