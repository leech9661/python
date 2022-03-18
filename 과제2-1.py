import turtle
import random
#2018038089 이광희 과제 2-1 
def  screenRightClick(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)
    r = random.random()
    g = random.random()
    b = random.random()
    tAngle = random.randrange(0,360)
    turtle.left(tAngle)
    tSize = random.randrange(1, 4)
    turtle.color((r, g, b))
    turtle.shapesize(tSize)
    turtle.penup()
    turtle.goto(x, y)
    turtle.stamp()

pSize = 5
r, g, b = 0.0, 0.0, 0.0

turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenRightClick, 3)

turtle.done()
