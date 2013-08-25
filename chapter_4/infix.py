
def in_to_pos(exp):
    list_exp = list(exp)
    list_mov = []
    list_final = []
    for c in list_exp:
        if c in ['*','/','+','-']: #poderia usar o c in
            if not len(list_mov):
                list_mov.append(c)
            else:
                if list_mov[-1] in ['*','/'] or (list_mov[-1] in ['+', '-'] and c in ['+', '-']):
                    list_final.append(list_mov.pop())
                list_mov.append(c)
        else:
            list_final.append(c)
    if len(list_mov):
        for m in list_mov[::-1]:
            list_final.append(m)
    return ''.join(list_final)


print in_to_pos('a*b*c')

#o split so presta se tiver espaco em branco, se nao a melhor forma de transformar string em lista e usando list.

