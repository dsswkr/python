# 실력 향상 예제 63
import random

num = random.randint(1, 100)

for i in range(5):
  get = int(input("1~99 사이의 추측 값을 입력하세요: "))
  if num > get:
    print("그것보다 큽니다.")
  elif num < get:
    print("그것보다 작습니다.")
  else:
    print("정답입니다!")
    exit(0)
print("실패했습니다!")

