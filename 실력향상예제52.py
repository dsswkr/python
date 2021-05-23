# 실력 향상 예제 52

names = [] 
scores = [[],[],[]]

for i in range(3):
  names.append(input("%i번 학생 이름을 입력하시오: " %(i+1)))
  scores[i].append(int(input("국어 점수를 입력하세요: ")))
  scores[i].append(int(input("영어 점수를 입력하세요: ")))
  scores[i].append(int(input("수학 점수를 입력하세요: ")))
  scores[i].append((scores[i][0] + scores[i][1] + scores[i][2]) / 3)  # 평균

print("----------------")
print("이름      : 평균")
print("----------------")

for i in range(3): 
  print("%-10s: %.2f" %(names[i], scores[i][3]))
