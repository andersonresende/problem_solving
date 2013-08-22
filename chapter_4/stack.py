
class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        #return True if self.items else False
        return self.items == []

    def size(self):
        return len(self.items)

class OtherStack(Stack):
    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]


def revstring(s1):
    stack = Stack()
    s2 = ''
    for c in s1:
        stack.push(c)
    while not stack.isEmpty:
        s2 += stack.pop()
    return s2





def main():
    # s = Stack()
    # print(s.isEmpty())
    # s.push(4)
    # s.push('dog')
    # print(s.peek())
    # s.push(True)
    # print(s.size())
    # print(s.isEmpty())
    # s.push(8.4)
    # print(s.pop())
    # print(s.pop())
    # print(s.size())
    from test import testEqual
    testEqual(revstring('apple'),'elppa')

main()
