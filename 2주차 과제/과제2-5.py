import turtle
#2018038089 이광희
num1, num2, res = 0, 0, 0
swidth, sheight = 1000, 500
curX, curY = 0, 0

def binaryToTurtle(binary, num):
    curX = swidth / 2

    for i in range(len(binary) - 2) :
        turtle.goto(curX, curY)
        if num & 1:
            turtle.color('red')
            turtle.turtlesize(2)
            turtle.stamp()
        else:
            turtle.color('blue')
            turtle.turtlesize(1)
            turtle.stamp()
        curX -= 50
        num >>= 1

if __name__ == "__main__":
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    num1, num2 = map(int, input("숫자를 2개 입력하세요 : ").strip().split(' '))
    curY = 0
    binaryToTurtle(bin(num1), num1)
    curY = -50
    binaryToTurtle(bin(num2), num2)
    curY = -100
    res = num1 & num2
    binaryToTurtle(bin(res), res)

turtle.done()

