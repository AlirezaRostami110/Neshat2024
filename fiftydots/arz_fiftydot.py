import random
import turtle
import time
from math import sqrt

myPen = turtle.Turtle()
screen = turtle.Screen()
screen.setup(800, 800)
myPen.speed(10)
myPen.color("black")
myPen.pensize(3)

myPen.penup()
myPen.goto(0, 0)
myPen.pendown()

def distance(list):
    radious = sqrt(list[0]**2 + list[1]**2)
    return radious

final_list = []

for i in range(49):
    x = (random.random()*400)*((-1)**random.randint(1,10))
    y = (random.random()*400)*((-1)**random.randint(1,10))
    final_list.append([x, y])

final_list = sorted(final_list, key= distance)

last_dot_num = random.randrange(-401,401)

final_dot_list = [[-400, last_dot_num], [last_dot_num, -400], [400, last_dot_num], [last_dot_num, -400]]



i = 0

while i<51 :
    color_names = ['red', 'orange', 'green', 'blue', 'purple', 'brown', 'pink', 'gray', 'black']
    random_color = random.choice(color_names)
    myPen.color(random_color)

    if i<49 :
        myPen.goto(final_list[i][0], final_list[i][1])
        i += 1
        continue
    elif i == 49 :
        last_dot = random.choice(final_dot_list)
        myPen.goto(last_dot[0], last_dot[1])
        i += 1
        time.sleep(5)
        break
