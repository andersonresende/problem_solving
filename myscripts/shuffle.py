def shuffle_len_3(st):
    """
    Recebe uma string de tamanho 3 e imprime seus embaralhamentos.
    :param st:string
    :return: None
    """
    def invert_last_two_terms_of_string(s1):
        """
        Recebe uma string de tamanho 3 e retornar duas strings com
        os uitimos dois caracteres embaralhados.
        :param s1:string
        :return: tuple
        """
        return s1, s1[0]+s1[1:][::-1]
    c = 0
    l1 = st[0]
    l2 = st[1]
    l3 = st [2]
    while c < 3:
        print(invert_last_two_terms_of_string(l1+l2+l3))
        c+=1
        l1,l2,l3 = l2,l3,l1


shuffle_len_3('abc')

