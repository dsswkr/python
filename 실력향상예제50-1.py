# 실력 향상 예제 50-1

def list_sort(a):
  length = len(a)-1
  for i in range(length):
    for j in range(length-i):
      if a[j] > a[j+1]:
        a[j], a[j+1] = a[j+1], a[j]
  return a

names = []

print("이름을 열 개 입력받아서 정렬한 내용을 출력합니다.")
for i in range(10):  
  names.append(input("이름을 입력하세요: "))

s_names = list_sort(names)

for i in range(10):  
  print("%2i: %s" %(i+1, names[i]))
