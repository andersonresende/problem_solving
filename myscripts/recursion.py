# -*- coding: utf-8 -*-

# 1)Pra que serve o return em uma recurção?
# return só deve ser usado quando precisamos do valor para efetuar alguma operação.


def ida(n):
    if n <= 5:
        print n
        ida(n+1)

#ida(0)


#2)pra onde uma volta da funcao recursiva volta?
# sempre pra o mesmo ponto (a sua chamada)

# se vc der um print em uma chamada que nao retorne nada ele dara None


# 3) codigo substituto
# não precisa usar pass, use a condição oposta a condição limite. ;)

# def do(valor):
#     if valor == 10:
#         pass
#     else:
#         do(valor+1)
#
# def do(valor):
#     if valor < 10:
#         do(valor+1)


# Recurcão básica

# 4) Calculo do Limite, voltas validas e invalidas
def loop(n, limit):
    if n < limit: # isso que determina a quantidade de voltas, assim como em um for comum, sempre lembrar que a recursao da as voltas validas + uma volta invalida que e quando ela retorna.
        print n
        loop(n+1, limit)


loop(1, 5)


# 5) Regra do print, prova que independente de onde a variavel esteja em uma volta da recursao o seu valor e o mesmo.



def somar(lst):
    if lst:
        # total = lst[0] + somar(lst[1:])
        # return total
        #linha que simplifica a linha comentada acima
        return lst[0] + somar(lst[1:]) # a ideia aqui e muito simples sempre o primeiro elemento + a soma dos outros.
    return 0

print somar([1,2,3])


# Recursive Fibonnaci com memozation
# Os exemplos servem pra entender a tecnica de evitar voltas desnecessarias usando if.

# Exemplo 1
def fibo_memo1(n):
    dc = {}

    def fibonnaci(n):
        if n <= 2:
            return 1
        else:
            # o problema que se o valor nao existir
            # ele verifica e ainda entra e ainda tem q retornar.
            # mas se ja existir e mais eficiente do que o exemplo abaixo.
            first = dc[n-1] if n-1 in dc else fibonnaci(n-1)
            second = dc[n-2] if n-2 in dc else fibonnaci(n-2)
            dc[n] = second + first
            return dc[n]

    return fibonnaci(n)

# Exemplo 2
def fibo_memo2(n):
    dc = {}

    def fibonnaci(n):
        if n <= 2:
            return 1

        if n in dc:
            return dc[n]

        dc[n] = fibonnaci(n-1) + fibonnaci(n-2)
        return dc[n]

    return fibonnaci(n)
