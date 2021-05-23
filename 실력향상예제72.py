# 실력 향상 예제 72

MAX = 100
COUNT = 20

n = 0			                # 구한 소수 개수 
check = [0 for i in range(MAX + 2)]     # 소수 거르는 리스트 (항목의 소수 상태)
prime_num = [0 for i in range(COUNT+2)] # 소수를 저장할 리스트 

for i in range(2, MAX+1):	        # 2부터 배수 검사
  if n >= COUNT:
    break
  if check[i] == 0:	        # 2부터 체크하여 리스트 항목 값이 0이면 소수임
    prime_num[n] = i
    print("%i " %i)                     # 소수 저장 및 출력
    n += 1
    for j in range(i, MAX+1, i):	# 배수는 소수가 아님 
      check[j] = 1
    
        
