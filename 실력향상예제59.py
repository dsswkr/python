# 실력 향상 예제 59

n = [45, 50, 70, 85, 90, 100]	    #짝수 개수 테스트
n2 = [45, 50, 65, 70, 85, 90, 100]  #홀수 개수 테스트 

count = len(n)
total = 0

print("\n점수: ", end='')
for i in range(count): 
  total += n[i]
  print("%i " %n[i], end='')
	
print("\n-------------------------------------------")

if count % 2:   # 항목이 홀수
  mid = int(count/2 + 1)
  print("중간 값은 %i, 점수 평균은 %i입니다." %(n[mid-1], total/count))
else:           # 항목이 짝수
  mid = int(count/2)
  print("중간 값은 %i, 점수 평균은 %i입니다." %((n[mid-1]+n[mid])/2, total/count))

print("-------------------------------------------")
