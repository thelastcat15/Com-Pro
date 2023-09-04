from turtle import *

width = 55

pencolor("green")

penup()
sety(-160)
pensize(5)
pendown()
sety(-30)
setx(width/2)
fillcolor("green")
begin_fill()
for _ in range(6) :
    left(60)
    forward(width)
end_fill()

goto(3,-3)
pencolor("white")
write("STOP", False, align="center", font=("MS Serif", 24, "bold"))

input()