import math
import random
def distance(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
p1 = [int(input("X: ")), int(input("Y: "))]
worldsize = int(input("World Size(Square): "))
t1 = [random.randint(0, worldsize), random.randint(0, worldsize)]
t2 = [random.randint(0, worldsize), random.randint(0, worldsize)]
t3 = [random.randint(0, worldsize), random.randint(0, worldsize)]



d1 = distance(p1[0], p1[1], t1[0], t1[1])
d2 = distance(p1[0], p1[1], t2[0], t2[1])
d3 = distance(p1[0], p1[1], t3[0], t3[1])

while d1 == d2 or d1 == d3 or d2 == d3:
    t1 = [random.randint(0, worldsize), random.randint(0, worldsize)]
    t2 = [random.randint(0, worldsize), random.randint(0, worldsize)]
    t3 = [random.randint(0, worldsize), random.randint(0, worldsize)]
    d1 = distance(p1[0], p1[1], t1[0], t1[1])
    d2 = distance(p1[0], p1[1], t2[0], t2[1])
    d3 = distance(p1[0], p1[1], t3[0], t3[1])



for x in range(worldsize):
    for y in range(worldsize):
        if distance(x, y, t1[0], t1[1]) == d1 and distance(x, y, t2[0], t2[1]) == d2 and distance(x, y, t3[0], t3[1]) == d3:
            print ("X: " + str(x))
            print ("Y: " + str(y))
        y += 1
    x += 1