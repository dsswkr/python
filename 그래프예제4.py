# 그래프  예제 4

import turtle as t

n = 6              # n 각형 
angle = 360/n      # 회전 각도 

t.reset()
t.color("red")
t.forward(100)
for i in range(n-1):
  t.left(angle)
  t.forward(100)

# 다음처럼 파이썬 터틀 함수를 이용해도 다각형을 그릴 수 있습니다. (예제는 6각형)
# t.circle(100,steps=6)

