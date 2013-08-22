

def myPyAnagram(s1, s2):
    return True if sorted(s1) == sorted(s2) else False


def myAnagram(s1, s2):
    """
    Recebe duas strings e compara se elas possuem os mesmo caracteres.
    O algoritimo falha pois ele procura para cada caractere da primeira
    o mesmo na segunda, sem levar em conta a quantidade de ocorrencias
    do caracter. Logo s1='aaa' e s2='abc' retornaria True.

    :param s1: string
    :param s2: string
    :return: boolean
    """
    ana = True
    for c1 in s1:
        if ana:
            ana = False
            for c2 in s2:
                if c1 == c2:
                    ana = True
                    break
        else:
            break
    return ana


def anagramSolution1(s1, s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 += 1

    return stillOK


def anagramSolution4(s1,s2):
    """
    Funcao muito boa pois conta exatamente a ocorrencia de cada termo nas
    duas strings e depois compara posicao por posicao para ver se batem. Assim
    evita que strings com caracteres alem dos da primeira string retornem True.

    :param s1: string
    :param s2: string
    :return: boolean
    """
    c1 = [0]*26
    c2 = [0]*26

    for i in range(len(s1)):
        pos = ord(s1[i])-ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i])-ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    stillOK = True
    while j<26 and stillOK:
        if c1[j]==c2[j]:
            j = j + 1
        else:
            stillOK = False

    return stillOK


def myWlAnagramFixed(s1, s2):
    #nao usar len(),
    #usar while
    #nao usar break
    b = True
    c1 = 0
    s2 = list(s2)
    while c1 < len(s1) and b:
        b = False
        c2 = 0
        while c2 < len(s2) and not b:
            if s1[c1] == s2[c2]:
                s2[c2] = None
                b = True
            c2 += 1
        c1 += 1
    if b:
        c2 = 0
        while c2 < len(s2) and b:
            if s2[c2]:
                b = False
            c2 += 1
    return b


def main():
    #print(anagramSolution1('adbc','dcba'))
    #print(myAnagram('aaaa','abc'))
    #print(myPyAnagram('aythg','atygh'))
    print(myWlAnagramFixed('abc','abc'))

main()