from turtle import *
from math import sqrt

loop = int(input("Loop : "))
if loop < 5 :
    print("Not Star")
    exit()

size = int(input("Size : "))
speed(int(input("Speed : ")) or 1)
pensize(3)

o = 18
if (loop % 2) :
    deg = 180/loop
    side = size*sqrt(2) - o

    penup()
    goto(0, size)
    right(90-deg/2)
    pendown()
    for _ in range(loop) :
        forward(side)
        penup()
        forward(o*2)
        pendown()
        forward(side)
        right(180-deg)
else :
    pass



input()