# 실력 향상 예제 55

LIMIT = 5000

for i in range(LIMIT+1):
  if ((i*i) > LIMIT): 
    n = i-1;
    break;

print("제곱 값이 5,000을 넘지 않는 가장 큰 정수는 %i입니다." %n)
print("%i의 제곱 값 = %i" %(n, n*n))
