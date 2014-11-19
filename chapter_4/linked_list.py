# -*- coding:utf-8 -*-

'''
Propriedades de linked lists:
    1. A linked list e criada atraves da ligação entre nos internamente, ou seja,
    a classe recebe um nó que esta ligado a outros nós.
    2 - A lista não armazena valores. Os valores estão contido nos nós.
'''


class Node(object):
    '''
    O no e necessario pq tiramos dos itens utilizados no encadeiamento
    a responsabilidade de receberem eles mesmos como parametros, quebrando
    a semantica do class. A lista não receberia outra lista. Uma lista
    receberia sempre valores, como uma list em python.
    '''
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList(object):
    '''
    Essa classe nos mostra que apenas com o uso de classes podemos
    construir uma lista igual a default em python.
    '''
    def __init__(self):
        #sempre o ultimo item
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def append(self, item):
        cont = 1
        size = self.size()
        head = self.head
        while cont < size:
            head = head.next
            cont+=1
        head.next = Node(item)

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        else:
            cont = 0
            next = self.head
            while pos-1 != cont:
                next = next.next
                cont += 1
            new_item = Node(item)
            new_item.next = next.next
            next.next = new_item

    def pop(self):
        cont = 2
        size = self.size()
        head = self.head
        while cont < size:
            head = head.next
            cont+=1
        last_item = head.next
        head.next = None
        return last_item

    def index(self, item):
        cont = 0
        head = self.head
        while head.data != item:
            head = head.next
            cont+=1
        return cont

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def __iter__(self):
        """Generetor thats loop a list"""
        def rec(node):
            if node:
                yield node.getData()
                for n in rec(node.getNext()):
                    yield n
        return rec(self.head)


class OrderedList():

    def __init__(self):
        #sempre o ultimo item
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        '''
        Em python ao passar por um item do OR o outro nao e executado.
        :param item:
        :return:
        '''''
        if self.isEmpty() or item < self.head.data:
            tmp = Node(item)
            tmp.next = self.head
            self.head = tmp
        else:
            tmp = Node(item)
            current = self.head
            while current and tmp.data > current.data:
                anterior = current
                current = current.next
            anterior.next = tmp
            tmp.next = current

    def pop(self):
        cont = 2
        size = self.size()
        head = self.head
        while cont < size:
            head = head.next
            cont+=1
        last_item = head.next
        head.next = None
        return last_item

    def index(self, item):
        cont = 0
        head = self.head
        while head.data != item:
            head = head.next
            cont+=1
        return cont

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


if __name__ == '__main__':
    lst = UnorderedList()
    lst.insert(0,'a')
    # lst.append('b')
    # lst.append('c')
    # lst.append('d')
    print lst.head
    print lst.index(0)

    # def r(lst):
    #     if lst:
    #         yield lst[0] # na segunda volta o retorno nao e printado pq ele retorna a chamada pra o for abaixo e o yield x vai ser chamado.
    #         for x in r(lst[1:]):
    #             yield x

    # ge = r([1,2,3])
    # print ge.next()
    # print ge.next()
    # print ge.next()
    # print ge.next()
    # ul = OrderedList()
    # ul.add(8)
    # ul.add(1)
    # ul.add(2)
    # ul.add(3)
    # ul.add(6)

    # print ul.index(1)
    # print ul.index(2)
    # print ul.index(3)
    # print ul.index(8)
    # print ul.index(6)




