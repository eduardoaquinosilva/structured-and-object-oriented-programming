frase = input().lower().split()
if len(frase) > 100:
    exit()
for a in frase:
    if '-' in a:
        a = list(a)
        a.remove('-')
        a = ''.join(a)
    if '.' in a[:len(a) - 2]:
        print('float', end=' ')
    elif a.isnumeric():
        b = int(a)
        print('int', end=' ')
    else:
        print('str', end=' ')
