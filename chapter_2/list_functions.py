

#BIG-O linear
def min_number_list_n(lista):
    """
    Funcao que retorna o menor valor dentro de uma lista de forma linear.

    :param lista:list
    :return:int
    """
    oin = lista[0]
    for n in lista[1:]:
        if n < oin:
            oin = n
    return oin


#BIG-O quadratica
def min_number_list_n2(lista):
    """
    Funcao que retorna o menor valor dentro de uma lista de forma quadratica.

    :param lista:list
    :return:int
    """
    for n in lista:
        for i in lista:
            if n > i:
                oin = False
                break
            oin = True
        if oin:
            break
    return n



print(min_number_list_n2([6, 5, 2, 5, 7,9,10,12,3,4,8,1]))

