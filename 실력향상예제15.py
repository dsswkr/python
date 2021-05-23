# 실력 향상 예제 15

num = -9999

while num < -100 or num > 100:
  num = int(input("정수를 입력하세요.(-100~100): "))

print("정수 = %i" %num)   

if num > 0:
  print("양수")
elif num == 0:
  print("영")
else:
  print("음수")
  
