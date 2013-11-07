import turtle

# myTurtle = turtle.Turtle()
# myWin = turtle.Screen()

# def drawSpiral(myTurtle, lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.left(90)
#         drawSpiral(myTurtle,lineLen+5)

# drawSpiral(myTurtle,300)
# myWin.exitonclick()


def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(40)
    t.up()
    t.backward(50)
    t.down()
    t.color("blue")
    tree(100,t)
    myWin.exitonclick()

main()
