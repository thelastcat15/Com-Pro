from turtle import *

# ============================
n_circle = 5
colors = ["blue", "yellow", "black", "green", "red"]
radius = 40
dis_X = 45
dis_Y = 20
penSize = 5
# ============================

penup()
Start_X = ((n_circle - 1) * dis_X) / 2
setx(-Start_X)
pensize(penSize)
for i in range(n_circle) :
    pencolor(colors[i])
    sety(dis_Y)
    pendown()
    circle(radius)
    penup()
    sety(-dis_Y)
    forward(dis_X)
    dis_Y *= -1

    

input()