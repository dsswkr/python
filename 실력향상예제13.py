# 실력 향상 예제 13

score = -1

while score < 0 or score > 100:
  score = int(input("점수를 입력하세요.(0~100): "))

print("점수 = %i" %score)   

if score >= 90:
  print("우수")
elif score < 60:
  print("탈락")

  
