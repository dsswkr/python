# 그래프  예제 1

import math
import turtle as t

SIZE = 100
high = int(math.sqrt(SIZE*SIZE - (SIZE/2)*(SIZE/2)))

t.reset()
t.color("red")
t.setx(SIZE)
t.goto(SIZE/2, high)
t.goto(0,0)


