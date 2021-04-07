import turtle as t
import math
t.shape('turtle')

t.penup()
t.goto(-360,0) #선그어지는것 없이 -360로 거북이 이동시킵니다.
t.pendown()

for x in range(-360,360): #sin그래프를 그립니다.
    y =math.sin(math.radians(x))*100 #곱 100하는 이유는 크기를 크게해주기위함
    t.goto(x,y)

t.done()