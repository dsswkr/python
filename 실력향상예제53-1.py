# 실력 향상 예제 53-1

def factorial( num ):
  if num < 1:
    return 1
  return factorial(num - 1) * num

n = 0

while n < 1 or n > 20: 
  n = int(input("팩토리얼 값을 구하고 싶은 정수를 입력하시오(1~20): "))
 
print("%i! = %d" %(n, int(factorial(n))))

