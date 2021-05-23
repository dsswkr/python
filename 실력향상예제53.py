# 실력 향상 예제 53

MAX  = 20
MIN  = 1

n = MAX + 1
factorial = 1

while n < MIN or n > MAX: 
  n = int(input("팩토리얼 값을 구하고 싶은 정수를 입력하시오(%i~%i): " %(MIN, MAX)))
  
for i in range(2, n+1):
  factorial *= i;
  
print("%i! = %d" %(n, factorial))

