class Deque:
    '''
    Deque podem ser usadas pra simulat comportamentos
    de filas e pilhas.
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def polindrome(s1):
    '''
    Este polindromo usa uma Deque para simular 
    o comportamento de uma pilha.
    '''
    deque = Deque()
    s2 = ''
    for c in s1:
        deque.addRear(c)

    while not deque.isEmpty():
        s2+= deque.removeRear()

    return s1==s2


print polindrome('121')


