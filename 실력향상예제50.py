# 실력 향상 예제 50

names = []

print("이름을 열 개 입력받아서 정렬한 내용을 출력합니다.")
for i in range(10):  
  names.append(input("이름을 입력하세요: "))

names.sort()

for i in range(10):  
  print("%2i: %s" %(i+1, names[i]))

  




