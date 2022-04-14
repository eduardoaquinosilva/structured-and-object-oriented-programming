op_jog, num_dedos_jog1, num_dedos_jog2 = input(), int(input()), int(input())
soma = num_dedos_jog1 + num_dedos_jog2
if (op_jog == 'p' and soma % 2 == 0) or (op_jog == 'i' and soma % 2 != 0):
    print('Venceu')
else:
    print('Perdeu')
