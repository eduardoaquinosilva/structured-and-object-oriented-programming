frase = input().lower()
if len(frase) > 50:
    exit()
for a in frase:
    if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
        frase = frase.replace(a, 'v')
    elif a == ' ':
        pass
    else:
        frase = frase.replace(a, 'c')
print(frase)
