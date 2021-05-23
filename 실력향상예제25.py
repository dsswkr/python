# 실력 향상 예제 25

sum = 0
num = 1

while num != 0:
  num = int(input("1 이상의 정수를 입력하면 합계를 출력합니다(0: 끝): "))
  sum += num
  if num == 0:
    print("끝났습니다.")
  else:
    print("입력한 숫자들의 합은 %i입니다." % sum)

