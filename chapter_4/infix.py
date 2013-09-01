from stack import Stack


def greater_element(dict_pounds):
    """
    Funcao que recebe um dicionaio com pesos para cada item e retorna
    o maior item por peso, usando assim a tecnica de pesos.
    :param dict_pounds: dicionario com items e pesos
    :return: string: contendo o item que possui maior peso
    """
    list_items = [k for k in dict_pounds]
    while len(list_items) > 1:
        if not dict_pounds[list_items[-1]] < dict_pounds[list_items[-2]]:
            list_items[-1], list_items[-2] = list_items[-2], list_items[-1]
        list_items.pop()
    return list_items.pop()


print greater_element({'c': 3, 'a': 1, 'b': 2, 'e': 5, 'd': 4})


def infix_to_postfix(exp):
    """
    Funcao que recebe uma expressao matematica infix e retorna sua postfix. Utiliza
    uma tecnica de Pesos para comparar os sinais utilizados nas expressoes.
    :param exp: string
    :return: string
    """
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    list_exp = list(exp)
    list_mov = []
    list_final = []
    for c in list_exp:
        if c in ['*','/','+','-']:
            if not len(list_mov):
                list_mov.append(c)
            else:
                if prec[list_mov[-1]] >= prec[c]:
                #if list_mov[-1] in ['*','/'] or (list_mov[-1] in ['+', '-'] and c in ['+', '-']):
                    list_final.append(list_mov.pop())
                list_mov.append(c)
        else:
            list_final.append(c)
    if len(list_mov):
        for m in list_mov[::-1]:
            list_final.append(m)
    return ''.join(list_final)


print infix_to_postfix('a*b*c*d')


def infixToPostfix(infixexpr):
    prec = {} #poderia inicializar tudo aqui
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split() #poderia usar um list aqui, assim nao necessitaria dos espacos

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789": #poderia estar tudo em uma so string, sem o or
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


print infixToPostfix("( A + B + C )")
print infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )")


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print postfixEval('7 8 + 3 2 + /')
