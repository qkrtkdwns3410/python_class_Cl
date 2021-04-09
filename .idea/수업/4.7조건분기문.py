#터틀 그래픽을 활용하여 원점을 중심으로 가로 세로 200크기의 사각형을 그린다
#마우스 이벤트를 사용하여 사각형 내부를 클릭하면 클릭한 지점에 파랑색 원,외부를 클릭하면 빨강색 원을 그린다
#원의 크기는 5입니다.



import turtle as t
import math

t.shape('turtle')
#사각형 그리기
t.penup()
t.goto(100,100)
t.pendown()
for i in range(4):
    t.right(90)
    t.forward(200)
def decision(x,y):
    t.penup()
    t.goto(x-10,y-10)
    t.pendown()
    if 100>=x>=-100 and 100>=y>=-100:

        t.pencolor("Blue")
        t.circle(20)
    else:
        t.pencolor("Red")
        t.circle(20)



t.onscreenclick(decision)
t.done()

