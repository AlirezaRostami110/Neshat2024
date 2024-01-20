import turtle
PROGNAME = 'Sierpinski Carpet'

myPen = turtle.Turtle()
myPen.speed(200)
myPen.color("#000000")


# This function draws a box by drawing each side of the square and using the fill function
def box(boxSize):
    myPen.begin_fill()
    myPen.forward(boxSize)
    myPen.left(90)
    myPen.forward(boxSize)
    myPen.left(90)
    myPen.forward(boxSize)
    myPen.left(90)
    myPen.forward(boxSize)
    if boxSize == 1400 :
        myPen.setheading(0)
    else :
        myPen.end_fill()
        myPen.setheading(0)

def boxlocation(length, width, boxSize, step):
    myPen.penup()
    myPen.goto(length,width)
    myPen.pendown()
    box(boxSize)
    if step > 0 :
        boxlocation(length-boxSize*2/3, width-boxSize*2/3, boxSize/3, step-1)
        boxlocation(length-boxSize*2/3, width+boxSize/3, boxSize/3, step-1)
        boxlocation(length-boxSize*2/3, width+boxSize*4/3, boxSize/3, step-1)
        boxlocation(length+boxSize/3, width+boxSize*4/3, boxSize/3, step-1)
        boxlocation(length+boxSize*4/3, width+boxSize*4/3, boxSize/3, step-1)
        boxlocation(length+boxSize*4/3, width+boxSize/3, boxSize/3, step-1)
        boxlocation(length+boxSize*4/3, width-boxSize*2/3, boxSize/3, step-1)
        boxlocation(length+boxSize/3, width-boxSize*2/3, boxSize/3, step-1)


myPen.penup()
myPen.goto(-700,-700)
myPen.pendown()

box(1400)
#if you want to change the step of square fractal you can edit step (the last arg of boxlocation() function)
boxlocation(-700/3, -700/3, 1400/3, 3)
