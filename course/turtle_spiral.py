import turtle
t = turtle.Turtle()
w = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen - 5)

drawSpiral(t, 100)
w.exitonclick()
