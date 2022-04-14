alcool, gasolina, rend_alcool, rend_gasolina = [float(i) for i in input().split()]
if 0.01 > alcool > 10 or 0.01 > gasolina > 10 or 0.01 > rend_alcool > 20 or 0.01 > rend_gasolina > 20:
    exit()
cust_alcool, cust_gasolina = alcool / rend_alcool, gasolina / rend_gasolina
if cust_alcool >= cust_gasolina:
    print('G')
else:
    print('A')
