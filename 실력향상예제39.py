# 실력 향상 예제 39

import math

a = 3
b = 4
c = 5;

s = (a + b + c) / 2.0
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print("각 변의 길이가 %i, %i, %i인 삼각형 넓이 = %.3f" %(a, b, c, area))

