from turtle import *

colors = ["blue", "yellow", "black", "Brown", ""]

penup()
goto()

for i in range(5) :
    penup()
    pencolor(colors[i])

    sety()

    pendown()
    circle(50)