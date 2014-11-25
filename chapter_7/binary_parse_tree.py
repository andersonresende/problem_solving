#! -*- coding: utf-8 -*-
import operator
from binary_tree_class import BinaryTree


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


def buildParseTree(fpexp):
    """ Função que recebe uma operação aritmetica e constroi uma árvore """

    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    return eTree


def evaluate(parseTree):
    """ Função que recebe uma árvore aritimética e retorna o resultado da operação """

    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


pt = buildParseTree("( ( 10 + 5 ) * 3 )")

print evaluate(pt)

