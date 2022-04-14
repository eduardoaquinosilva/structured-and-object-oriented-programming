n1, n2, simb = int(input()), int(input()), input()
if simb == '+':
    print(n1 + n2)
elif simb == '-':
    print(n1 - n2)
elif simb == '*':
    print(n1 * n2)
elif simb == '/':
    try:
        print(n1 // n2)
    except:
        print('invalida')
else:
    exit()
