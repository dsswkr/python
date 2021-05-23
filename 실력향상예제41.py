# 실력 향상 예제 41

LIMIT = 1000
n = 0

for i in range(1, LIMIT):
  n += i		# 합 계산
  if( n >= LIMIT ):     # 합이 1000을 넘어가면 for 블록 중지
    break;

print("1~n 합이 1,000을 넘어가는 가장 작은 정수 n = %i" %(i))

