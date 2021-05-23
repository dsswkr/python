# 그래프  예제 8

import math
import turtle as t

START_X = -200
START_Y = 0
P_SIZE = 2

ta = [ 220, 190, 150, 310 ]

t.reset()
t.color("black")

# X축, Y축 기준선 그리기
t.penup()
t.goto(START_X, 350)
t.pendown()
t.goto(START_X, 0)
t.goto(START_X+500, START_Y)
  
# 꺾은선 그래프 그리기
t.penup()
t.color("red")

for i in range(4):
  x = START_X + (i+1)*100
  y = ta[i]
  t.goto(x, y)
  if i == 0:
    t.pendown()  
  t.circle(P_SIZE)

t.hideturtle()











