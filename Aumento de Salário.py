salario = float(input())
if salario <= 1000:
    novo_salario = salario * 1.2
elif 1000 < salario <= 1500:
    novo_salario = salario * 1.15
elif 1500 < salario <= 2000:
    novo_salario = salario * 1.1
else:
    novo_salario = salario * 1.05
print(f'{novo_salario:.2f}')
