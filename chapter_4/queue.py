class Queue(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def fighter_league(dict_fighters):
    """
    Funcao que simula um campeonato usando uma fila em que os lutadores
    competem de dois em dois ate chegar a um vencedor.
    :param dict_fighters: dicionario com lutadores e seus pesos
    :return: str: nome do lutador vencedor
    """
    queue = Queue()
    [queue.enqueue(f) for f in dict_fighters]
    while queue.size() > 1:
        f1 = queue.dequeue()
        f2 = queue.dequeue()
        winner = f1 if dict_fighters[f1] > dict_fighters[f2] else f2
        queue.enqueue(winner)
    return queue.dequeue()

print fighter_league({'a': 10, 'b': 13, 'c': 7, 'd': 5})


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)
    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()

print hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 8)





