soma = 0
for i in range(4):
    soma += int(input())
if soma == 0:
    print('nenhum')
elif soma <= 4:
    print(f'jog{soma}')
else:
    jog = soma % 4
    if jog == 0:
        print('jog4')
    else:
        print(f'jog{jog}')
