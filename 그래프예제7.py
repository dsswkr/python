# 그래프  예제 7

import math
import turtle as t

R = 100.0
START_X = -200
START_Y = 0

t.reset()
t.color("black")

# X축, Y축 기준선 그리기
t.penup()
t.goto(START_X - 20, 0)
t.pendown()
t.goto(200+20, 0)
t.penup()
t.goto(START_X, START_Y+200)
t.pendown()
t.goto(START_X, START_Y-200)
  
# 사인 그래프 그리기
t.penup()
t.goto(START_X, START_Y)
t.pendown()

t.color("red")

for i in range(361):
  radian = (i*3.14159) / 180
  x = i + START_X
  y = math.sin(radian) * R + START_Y
  t.goto(x, y)   # goto(i + START_X, sin(radian) * R + START_Y)

t.hideturtle()











