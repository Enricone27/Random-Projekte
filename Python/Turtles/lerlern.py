from turtle import *
speed(0)
a=360
for i in range(a*2):
    forward(i/360)
    left(a/360)
    pencolor(1,0,0)

penup()
goto(0,0)
pendown()
for i in range(a*2):
    forward(i/360)
    right(a/360)
    pencolor(0,1,0)

penup()
goto(0,0)
pendown()
for i in range(a*2):
    forward(-i/360)
    left(a/360)

penup()
goto(0,0)
pendown()
for i in range(a*2):
    forward(-i/360)
    left(-a/360)
done()