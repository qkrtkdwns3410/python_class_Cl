import turtle as t
import math
t.shape('turtle')

t.penup()
t.goto(-360,0)
t.pendown()

for x in range(-360,360):
    y =math.sin(math.radians(x))*100
    t.goto(x,y)

t.done()