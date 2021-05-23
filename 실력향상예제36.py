# 실력 향상 예제 36
import math

d = 100.0
h = d * math.sin(math.radians(30)) * math.sin(math.radians(40))
h /= math.sin(math.radians(40-30))

print("피라미드 높이는 %.1fm입니다." %h)
