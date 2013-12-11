import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def func_sum(lineLen):
	return lineLen + 5
def func_sub(lineLen):
	return lineLen - 5

def drawSpiral(myTurtle, lineLen, func):
    if lineLen > 0:
        myTurtle.forward(lineLen) # em frente
        myTurtle.left(90)
        drawSpiral(myTurtle,func(lineLen), func)

drawSpiral(myTurtle,50, func_sub)
myWin.exitonclick()


# def tree(branchLen,t):
#     if branchLen > 5:
#         t.forward(branchLen)
#         t.right(20)
#         tree(branchLen-15,t)
#         t.left(40)
#         tree(branchLen-15,t)
#         t.right(20)
#         t.backward(branchLen)

# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     t.left(90)
#     t.up()
#     t.backward(100)
#     t.down()
#     t.color("green")
#     tree(150,t)
#     myWin.exitonclick()

# main()

# import random

# def crazy_turtle(turtle, len_street):
#     if len_street < 1:
#         return 0

#     i = random.choice([1, 2, 3, 4])

#     if i == 1:
#         turtle.forward(len_street/100)
#     elif i ==2:
#         turtle.right(len_street/100)
#     elif i == 3:
#         turtle.backward(len_street/100)
#     else:
#         turtle.left(len_street/100)

#     crazy_turtle(turtle, len_street - i)


# # def main():
# #     t = turtle.Turtle()
# #     myWin = turtle.Screen()
# #     t.forward(500)
# #     t.left(90)
# #     t.forward(300)
# #     t.backward(600)
# #     t.forward(300)
# #     t.left(90)
# #     t.forward(700)
# #     t.right(180)
# #     #
# #     crazy_turtle(t, 5000)
# #
# # main()


# def quad(t, len, p):
#     if len:
#         t.forward(len)
#         t.right(90)
#         t.forward(len)
#         t.right(90)
#         t.forward(len)
#         t.right(90)
#         t.forward(len)
#         t.right(90)
#         if p==1:
#             quad(t, len/2, p+1)
#         if p==2:
#             t.forward(len)
#             quad(t, len, p+1)
#             t.right(90)
#             t.forward(len*2)


# def main():
#     t = turtle.Turtle()
#     myWin = turtle.Screen()
#     quad(t, 300, 1)

# main()







