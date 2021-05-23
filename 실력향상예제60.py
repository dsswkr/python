# 실력 향상 예제 60
import math

scores = [60, 70, 65, 85, 95, 88, 100, 75, 50]
mean = 0
variance = 0

count = len(scores) # 개수 구하기 
total = sum(scores) # 합계 구하기
mean = total/count  # 평균 구하기

print(scores)

for i in range(count):
  variance += (mean - scores[i])*(mean - scores[i])

variance /= count  # 분산 
std_deviation = math.sqrt(variance)  # 표준편차 

print("*평균 = %.3f\n*분산 = %.3f\n*표준편차 = %.3f" %(mean, variance, std_deviation))

