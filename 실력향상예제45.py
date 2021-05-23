# 실력 향상 예제 45

na = [ 20, -10, 5, -4, -11, 6, -1 ]
sum = 0

for i in range(len(na)): 
  print(na[i])
  if (na[i] < 0):
    sum += na[i]

print("\n음수 합 = %i" %sum)
