valor_quebrado, valor_negociado = input(), input()
if len(valor_negociado) > 100:
    exit()
for a in valor_negociado:
    if a == valor_quebrado:
        valor_negociado = valor_negociado.replace(a, '')
if valor_negociado == '':
    valor_negociado = 0
print(int(valor_negociado))
