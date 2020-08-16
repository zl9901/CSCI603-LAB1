import turtle
import math

# global constants for window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000

def init():
   
    turtle.setworldcoordinates(-WINDOW_WIDTH/2, -WINDOW_WIDTH/2,
        WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    turtle.up()
    turtle.title('Name')
    turtle.pen()
    turtle.down()
    #turtle.right()
    #turtle.left()

def drawZ():
    turtle.forward(50)
    turtle.right(135)
    turtle.forward(50*math.sqrt(2))
    turtle.left(135)
    turtle.forward(50)
    turtle.up()

def drawH():
    turtle.forward(25)
    turtle.down()
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(25)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.backward(50)
    turtle.up()
    turtle.right(90)
    turtle.forward(35)

def drawU():
    turtle.down()
    turtle.left(135)
    turtle.forward(10*math.sqrt(2))
    turtle.right(45)
    turtle.forward(40)
    turtle.backward(40)
    turtle.right(135)
    turtle.forward(10*math.sqrt(2))
    turtle.left(45)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(10*math.sqrt(2))
    turtle.left(45)
    turtle.forward(40)
    turtle.up()

def drawO():
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(35)
    turtle.down()
    turtle.left(135)
    turtle.forward(10*math.sqrt(2))
    turtle.right(45)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(10*math.sqrt(2))
    turtle.right(45)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(10*math.sqrt(2))
    turtle.right(45)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(10*math.sqrt(2))
    turtle.right(45)
    turtle.forward(30)
    turtle.up()

def drawL():
    turtle.right(180)
    turtle.forward(65)
    turtle.down()
    turtle.left(90)
    turtle.forward(50)
    turtle.backward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.up()

def drawI():
    turtle.forward(25)
    turtle.down()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.backward(50)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.up()
    turtle.forward(35)


def drawName():
    
    drawZ()
    drawH()
    drawU()
    drawO()
    drawL()
    drawI()
    drawU()
    turtle.done()
    
def mainloop():
    init()
    drawName()


if __name__ == "__main__":
    mainloop()

