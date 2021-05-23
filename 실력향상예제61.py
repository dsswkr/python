# 실력 향상 예제 61

MAX = 30
MIN = (-MAX)

def f(x):
  return (5 * x*x*x - 3 * x*x + 2 * x - 1)

a = MAX + 1
b = a

while a < MIN or a > MAX or b < MIN or b > MAX:
  a = int(input("-30~30 범위의 정수를 입력하시오: "))
  b = int(input("-30~30 범위의 정수를 입력하시오: "))       

print("f(%i) - f(%i) = %i" %(a, b, f(a)-f(b)))
