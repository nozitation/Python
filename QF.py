import math
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
x = (-b+math.sqrt((b*b)-4*a*c))/2*a
if (a*x*x+b*x+c) == 0:
    print('X: ' + str(x))