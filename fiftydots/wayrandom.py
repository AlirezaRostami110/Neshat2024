import math
import random
import turtle

myPen = turtle.Turtle()
screen = turtle.Screen()
myPen.color('#000000')
myPen.speed(5)

def change_color():
    red = random.random()
    green = random.random()
    blue = random.random()
    myPen.pencolor(red, green , blue)


def way(size, n):
    screen.setup(size,size)
    screen.tracer(0)
    r_range = size/10
    for i in range(n):
        change_color()
        myPen.up()
        myPen.goto(0, 0)
        myPen.down()
        myPen.left(360*random.random())
        myPen.forward(r_range*random.random())
        while abs(myPen.xcor()) < 400 and abs(myPen.ycor()) < 400:
            myPen.setheading(math.degrees(math.atan2(myPen.ycor(), myPen.xcor())))
            myPen.left(90 * ((-1) ** random.randint(1, 10)) * random.random())
            myPen.forward(r_range*random.random())
    screen.tracer(1)
    turtle.mainloop()
way(800,50)

