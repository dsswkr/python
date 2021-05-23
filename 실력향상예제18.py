# 실력 향상 예제 18  

sum = 0
for i in range (1, 101):
  if((i%3) == 0):   # 3으로 나눈 나머지가 0이면 3의 배수
    sum += i
print("1에서 100까지 3의 배수 합 = %i" %sum)

# 다른 방법
sum = 0
for i in range (3, 101, 3): # 3부터 3씩 증가하면 3의 배수
   sum += i
print("1에서 100까지 3의 배수 합 = %i" %sum)

# 공식을 이용한 방법
n = int(100/3)
sum = 3 * n * (n+1) / 2
print("1에서 100까지 3의 배수 합 = %i" %sum)
