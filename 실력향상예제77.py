# 실력 향상 예제 77

# 피보나치 수열 구하기

def fib(n):
    if(n <= 1):
        return 1    
    else:
        return fib(n-2) + fib(n-1)

num=10   # 10번째 항 = 55
print("피보나치 수열 %i번째 항 = %i" %(num, fib(num-1)))       

