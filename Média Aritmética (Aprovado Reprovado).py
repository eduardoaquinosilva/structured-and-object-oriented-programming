n1, n2 = float(input()), float(input())
media = (n1 + n2) / 2
print(f'{media:.1f}')
if media >= 7:
    print('Aprovado')
elif 7 > media <= 4:
    print('AF')
else:
    print('Reprovado')
