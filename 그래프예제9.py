# 그래프  예제 9

import math
import turtle as t

START_X = -200
START_Y = 0
UNIT_HIGHT = 30 

birth_data = [2, 4, 3, 5, 3, 6, 5, 2, 7, 5, 8, 3]

t.reset()
t.color("black")

# X축, Y축 기준선 그리기
t.penup()
t.goto(START_X, 350)
t.pendown()
t.goto(START_X, 0)
t.goto(START_X+550, START_Y)
  
# 막대 그래프 그리기
t.color("red")
t.pensize(20)
t.penup()

for i in range(12):
  x = START_X + (i+1)*40
  y = START_Y + 5
  t.goto(x, y)
  t.pendown()
  t.setheading(90)
  t.forward(birth_data[i]*UNIT_HIGHT)
  t.penup()

t.hideturtle()











