#sin 곡선 그리기.
import math #math내장함수
import turtle as t #터틀그래픽 선언

t.shape('turtle')#터틀그래픽 shape선언



def moveUp():
    t.setheading(90)
    t.forward(30)
def moveDown():
    t.setheading(270)
    t.forward(30)
def moveLeft():
    t.setheading(180)
    t.forward(30)
def moveRight():
    t.setheading(0)
    t.forward(30)


t.onkeypress(moveUp,"Up") #위쪽 방향키 입력시 왼쪽 90도 바라보고 30만큼 전진합니다.
t.onkeypress(moveDown,"Down")
t.onkeypress(moveLeft,"Left")
t.onkeypress(moveRight,"Right")



t.listen() #키보드 입력 이벤트 처리를 위하여 필요합니다.
t.done() #종료