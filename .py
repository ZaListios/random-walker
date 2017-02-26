from turtle import *
import math, random
ht()
penup()
setpos(100,100)
pendown()
setpos(100,-100)
setpos(-100,-100)
setpos(-100,100)
setpos(100,100)
penup()
setpos(0,0)
pendown()
while 1:
    yval = ycor()
    xval = xcor()
    a=random.randint(0, 3)
    if a == 0:
        pencolor("#ff0000")
        sety(yval+1)
    elif a == 1:
        pencolor("#00ff00")
        setx(xval+1)
    elif a == 2:
        pencolor("#0000ff")
        sety(yval-1)
    else:
        pencolor("#ff00ff")
        setx(xval-1)
    if xcor == 100:
        setx(-99)
    if ycor == 100:
        sety(-99)
    if xcor == -100:
        setx(99)
    if ycor == -100:
        sety(99)
