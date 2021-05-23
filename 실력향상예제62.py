# 실력 향상 예제 62

import random

nums = [0 for i in range(10)]

for i in range(100):
  num = random.randint(1, 9)
  nums[num] += 1
  print("%i, " %num, end='')

print("\n--------------------------------------------------------------\n")
for i in range(1,10):
  print("%i : %i" %(i, nums[i]))
