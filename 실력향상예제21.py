# 실력 향상 예제 21 

#-----------------------------------
# 메인 처리 
a = int(input("(1) 정수를 입력하세요: "))

b = a
while a == b:  # a와 b가 다를 때까지 반복
  b = int(input("(2) 두 번째 다른 정수를 입력하세요: "))

c = a
while c == b or c == a:  # c가 a, b와 다를 때까지 반복
  c = int(input("(3) 세 번째 다른 정수를 입력하세요: "))

# a, b, c의 값을 작은 수에서 큰 순서로 배치함 (중간 값은 b가 됨)
if a > b: 
  a,b = b,a
if b > c: 
  b,c = c,b
if a > b: 
  a,b = b,a

print("%i, %i, %i 값의 중간 값은 %i" %(a, b, c, b))



# 리스트를 이용하기
li = []  # 리스트 선언

a = int(input("(1) 정수를 입력하세요: "))

b = a
while a == b:  # a와 b가 다를 때까지 반복
  b = int(input("(2) 두 번째 다른 정수를 입력하세요: "))

c = a
while c == b or c == a:  # c가 a, b와 다를 때까지 반복
  c = int(input("(3) 세 번째 다른 정수를 입력하세요: "))

#리스트에 추가 
li.append(a)  
li.append(b)
li.append(c)

# 리스트의 sort 기능으로 정렬
li.sort()

print("%s 값의 중간 값은 %i" %(li, li[1]))
