# 실력 향상 예제 42

LIMIT = 10000
n = 0

for i in range(1, LIMIT):
  n += i		# 합 계산
  if( n >= LIMIT ):     # 합이 10,000을 넘어가면 for 블록 중지
    break;

print("1~n 합이 %i을 넘지 않는 가장 큰 정수 n = %i" %(LIMIT, i-1))

