# 실력 향상 예제 77-1

# 빠른 피보나치 수열 구하기 

def fastFib(n, memo):
    if not n in memo:
        memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
    return memo[n]

def fibonacci(n):
    memo = {0:1, 1:1}
    return fastFib(n, memo)

num=10   # 10번째 항 = 55
print("피보나치 수열 %i번째 항 = %i" %(num, fibonacci(num-1)))   

