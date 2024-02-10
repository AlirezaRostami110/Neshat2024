import random
import math
import matplotlib.pyplot as plt

def distance(point):
    return math.sqrt(((point[0])**2) + ((point[1])**2))

def create_random_points():
    points = []
    points.append([0, 0])
    distance = 0
    radian = random.uniform(0, 2*math.pi)
    while distance < 400*(2**0.5):
        distance = random.uniform(distance, distance + 80)
        x = distance*math.cos(radian)
        y = distance*math.sin(radian)
        if distance < 400*(2**0.5):
            radian = random.uniform((radian-((math.pi)/8)), (radian+((math.pi)/8)))
        points.append([x, y])
        if (abs(x) > 400) or (abs(y) > 400) : 
            if abs(points[-1][0]) > 400:
                if points[-1][0] > 0:
                    points[-1][0] = 400
                else:
                    points[-1][0] = -400
            if abs(points[-1][1]) > 400:
                if points[-1][1] > 0:
                    points[-1][1] = 400
                else:
                    points[-1][1] = -400
            break
    print(points)
    return points

def connect_points(points):
    for i in range(1,len(points)):
        x1 = [points[i-1][0], points[i][0]]
        x2 = [points[i-1][1], points[i][1]]
        plt.plot(x2, x1, '-bo')

if __name__ == "__main__":
    for i in range(50):
        points_list = create_random_points()
        connect_points(points_list)
    plt.axis([-400, 400, -400, 400])
    plt.show()