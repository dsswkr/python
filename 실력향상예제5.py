# 실력 향상 예제 5

scores = [-1, -1, -1, -1, -1]
max_score = -1

for i in range(0, 5): 
  while (scores[i] < 0 or scores[i] > 100):
    scores[i] = int(input("(%i) 점수를 정수로 입력하시오(0~100): " %(i+1)))
  if(max_score < scores[i]):
    max_score = scores[i]

print("최고 점수는 %i점입니다." %max_score)

      

