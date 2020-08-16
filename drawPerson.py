import turtle
import math
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

def init():
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.title('Name')
    turtle.pen()
    turtle.down()


RADIUS=150
def drawHead(t,hairlength,hairangle):
    t.down()
    t.circle(RADIUS)
    t.left(90)
    t.up()
    t.forward(RADIUS)
    t.left(60)
    
    for x in range(0,5):
        t.forward(RADIUS)
        t.down()
        t.forward(hairlength)
        t.up()
        t.back(RADIUS+hairlength)
        t.right(hairangle)
    t.left(30*3)

def drawEyes(t,side,angle):
    t.right(30)
    t.forward(50)
    t.down()
    for y in range(0,3):
        t.forward(side)
        t.right(angle)
    t.up()
    t.back(50)
    t.left(60)

    t.forward(50)
    t.down()
    for z in range(0,3):
        t.forward(side)
        t.left(angle)
    t.up()
    t.back(50)
    t.right(30)


def drawNose(t,polyside,polyangle):
    t.down()
    t.right(90)
    t.forward(12)
    for z in range(0,4):
        t.left(polyangle)
        t.forward(polyside)
    t.left(72)
    t.forward(12)
    t.left(90)
    t.up()
    t.done()

def drawMouth(t):
    pass

def getEyesSize(RADIUS):
    return RADIUS/3

def getNoseSize(RADIUS):
    return RADIUS/6.25

def getHeadSize(RADIUS):
    return RADIUS/6

def getFaceSize(RADIUS):
    eyes=getEyesSize(RADIUS)
    nose=getNoseSize(RADIUS)
    head=getHeadSize(RADIUS)
    return eyes,nose,head

    
    
def main():
    t=turtle.Turtle()
    init()
    t.speed(5)
    eyes,nose,head=getFaceSize(RADIUS)
    #head=getHeadSize()
    #eyes=getEyesSize()
    #nose=getNoseSize()
    drawHead(t,head,30)
    drawEyes(t,eyes,120)
    drawNose(t,nose,72)


if __name__ == "__main__":
    main()
