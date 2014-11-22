

def map(f, lst):
    if not lst:
        return []
    return [f(lst[0])] + map(f, lst[1:])


def filter(f, lst):
    if not lst:
        return []

    if f(lst[0]):
        return [lst[0]] + filter(f, lst[1:])
    else:
        return filter(f, lst[1:])


def fold():
    """Funcao para ser estudada posteriormente, e mais complexa"""
    pass


print map(lambda x: x+1, [0, 1, 2, 3])
print filter(lambda x: x > 0, [0, 1, 2, 3])