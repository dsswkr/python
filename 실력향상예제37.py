# 실력 향상 예제 37

x = -1
y = -1

while (x < 1 or x > 9 or y < 2 or y > 10):
  print("X의 Y승 결과 및 그 자리 수를 구하는 예제입니다.")
  x = int(input("정수 X를 입력하세요(1~9): "))
  y = int(input("정수 Y를 입력하세요(2~10): "))

xy = x**y        
print("%i의 %i승 = %i" %(x, y, xy))
print("결과 값은 %i자리입니다." %len(str(xy))) 
