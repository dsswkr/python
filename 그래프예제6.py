# 그래프  예제 6

import math
import turtle as t

t.reset()
t.color("red")

# 집 그리기
t.penup()
t.goto(0, 0)
t.pendown()
t.setheading(0)

for i in range(4):
  t.forward(100)
  t.left(90)
  
t.penup()
t.goto(-50, 100)
t.pendown()
t.forward(200)
t.goto(50, 150)
t.goto(-50, 100)
t.hideturtle()



