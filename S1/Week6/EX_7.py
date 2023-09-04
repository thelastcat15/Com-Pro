from turtle import *

#ปรับได้
#----------------
radius = 50
num_circle = 3
disFromCenter = 20
#----------------

penup()
setheading(90) # หันขึ้นบน

colors = ["yellow", "blue", "red"]
change_degree = 360/num_circle
for i in range(num_circle) :
  pencolor(colors[i])
  forward(disFromCenter)
  left(90)
  pendown()
  circle(radius)
  penup()
  right(90)
  backward(disFromCenter)
  left(change_degree)

input()