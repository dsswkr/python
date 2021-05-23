# 실력 향상 예제 71

import math

MIN = 1
MAX = 20

for a in range(MIN, MAX+1):
  for b in range(MIN, MAX+1):
    a2b2 = a*a + b*b   
    c = int(math.sqrt(a2b2))
    cc = a2b2;

    if (cc == c*c):    # a*a + b*b = c*c 만족 
      print("A=%3i, B=%3i, C=%3i" %(a, b, c))
