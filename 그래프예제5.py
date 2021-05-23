# 그래프  예제 5

import math
import turtle as t

R = 100.0
START_X = 150
START_Y = 150

t.reset()
t.color("red")
t.penup()

# 원 그리기 

for i in range(0, 361): 
  radian = (i*3.14159) / 180
  x = math.cos(radian) * R + START_X
  y = math.sin(radian) * R + START_Y
  t.goto(x, y)
  t.pendown()

t.penup()
t.home()  

# 다음처럼 파이썬 터틀 함수를 이용해 원을 그릴 수 있습니다. 
# t.circle(100)




