# 실력 향상 예제 12-1

import math

for i in range(1, 21):
  k = math.log(i)*25.0
  print("%s*" %(" "*int(k)))    
    

# 다른 방식: 속도가 느림 
#for i in range(1, 21):
#  k = int(math.log(i)*25.0)
#  for j in range(k):
#    print(" ", end="")
#  print("*");  
    
