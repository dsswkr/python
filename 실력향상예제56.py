# 실력 향상 예제 56

MIN = 10
MAX = 100000

for i in range(len(str(MIN)), len(str(MAX))):
  for j in range(1,10):
      print("%s, " %(str(j)*i), end='')
  print()
  
