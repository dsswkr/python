# 실력 향상 예제 17

sum = 0
for i in range (1, 101):
  if((i%2) == 0):   # 2로 나눈 나머지가 0이면 짝수
    sum += i
print("1에서 100까지의 짝수 합 = %i" %sum)

# 다른 방법
sum = 0
for i in range (2, 101, 2): # 2부터 2씩 증가하면 짝수
   sum += i
print("1에서 100까지의 짝수 합 = %i" %sum)

# 공식을 이용한 방법
n = int(100/2)
sum = n*(n+1)
print("1에서 100까지의 짝수 합 = %i" %sum)
