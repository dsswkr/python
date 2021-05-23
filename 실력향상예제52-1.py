# 입력받은 점수가 정상일 때까지 입력받는 예제 

score = -1
while score < 0 or score > 100:
  score = int(input("국어 점수를 입력하세요: "))

print(score)
