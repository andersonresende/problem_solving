# -*- coding: utf-8 -*-
#!/usr/bin/env python


class BinaryTree(object):

    """ 
        Não usamos nodes para juntar as binarys trees porque 
        semanticamente não faz muito sentido e também porque 
        não haveria necessidade de colocar o valor root da 
        tree em um node. 
    """

    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
            #apenas existirao right em uma binary se houver left
            if self.rightChild:
                self.rightChild.preorder()

tree = BinaryTree('livro')
tree.insertLeft('cap.1')
tree.insertRight('cap.2')
tree.getLeftChild().insertLeft('sec1')
tree.getLeftChild().insertRight('sec2')


def preorder(tree):
    """Printa o pai e depois os filhos"""
    if tree:
        print(tree.getRootVal())
        if tree.getLeftChild():
            preorder(tree.getLeftChild())
            if tree.getRightChild():
                preorder(tree.getRightChild())


def postorder(tree):
    """Printa os filhos e depois o pai"""
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())


def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())


preorder(tree)
print "-------------------------"
postorder(tree)
print "-------------------------"
inorder(tree)


#pra que fazer uma recursao entrar em uma volta, sera que e preciso apenas quando desejamos retorno.


def sum_nested(lst):
    """Função recursiva que retorna a soma dos elementos de uma lista aninhada"""
    if not lst:
        return 0

    if not type(lst[0]) == list:
        total = lst[0] 
    else:
        total = sum_nested(lst[0]) 

    return total + sum_nested(lst[1:])

print sum_nested([1,1,1,1,[1,1,1,1]])

# Amanha somar todos os valores da tree, admitindo que todos sejam inteiros