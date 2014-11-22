#! -*- encoding:utf-8 -*-

"""
    Modulo que explica o uso de funcoes passadas como argumentos de forma legal.
"""


def double(x):
    """Funções simples podem ser trocadas por lambdas"""
    return x * 2


def increment(x):
    return x + 1


def n_times_to_value(f, x, n):
    if not n:
        return x
    return f(n_times_to_value(f, x, n-1))


def double_times(x, n):
    n_times_to_value(double, x, n)
    # a linha acima pode ser substituida por uma funcao lambda:
    # n_times_to_value(lambda a: a * 2, x, n)


def increment_times(x, n):
    n_times_to_value(increment, x, n)


