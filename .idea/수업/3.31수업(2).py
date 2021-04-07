# def func_sum(x1,x2): #함수 선언.
#     tot=0
#     for i in range(x1,x2+1): #x1부터 x2까지숫자를 더한 값을 tot에 담습니다.
#         tot+=i
#     print(tot)
# func_sum(3,5) #for (i 3..until 6)
#
# def func_tot(x):
#     tot=0 #초기화
#     for i in range(x+1):   #0부터 x까지의 숫자를 더한 값을 tot에 담습니다.
#         tot +=i
#     return tot #tot를 반환합니다.
# print("합계는: ",func_tot(10))

# 내장함수

#수학 관련 모듈
import math #보통 상단부에서 선언합니다.
print(math.sqrt(5)) #제곱근
print(math.pi) #파이값 출력
print(math.sin(math.radians(30)))#sin 30도 출력.

import random
for i in range(5):
    print(random.randint(1,10)) #1~10정수 난수 출력합니다
for i in range(7):
    print(random.random()) #7개의 소수점 아래의 난수 출력합니다.
