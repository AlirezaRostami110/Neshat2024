import random
import turtle

myPen = turtle.Turtle()
screen = turtle.Screen()
screen.setup(800, 800)
myPen.speed(50)
myPen.color("black")
myPen.pensize(2)
screen.tracer(0)
myPen.setheading(0)

for i in range(50): 
    myPen.penup()
    myPen.goto(0, 0)
    myPen.pendown()

    color_names = ['red', 'orange', 'green', 'blue', 'purple', 'brown', 'pink', 'gray', 'black']
    random_color = random.choice(color_names)
    myPen.color(random_color)

    dis = random.randrange(0,50)
    degree_0 = random.randrange(0,360)
    myPen.setheading(degree_0)
    j = 0

    if j == 0 :
        myPen.left(degree_0)
        myPen.forward(dis)
        j = 1
    
    while j == 1 :
        myPen.setheading(degree_0)
        degree = random.randrange(degree_0-45,degree_0+45)
        dis = random.randrange(dis,50)
        myPen.left(degree)
        myPen.forward(dis)
        myPen.setheading(degree_0)
        if abs(myPen.xcor()) >= 400 or abs(myPen.ycor()) >= 400 :
            break
turtle.mainloop()
screen.tracer(1)
