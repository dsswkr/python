# 리스트 만들기
import random

# 값이 없는 10개 항목을 가진 리스트 만들기 
mylist1 = [None] * 10

print(mylist1)

# 10개 항목의 값이 0인 리스트 만들기 
mylist2 = [0] * 10

print(mylist2)

# 연속된 값을 10개 가진 리스트 만들기 (예: 1~10)
mylist3 = [i for i in range(1, 11)]

print(mylist3)

# 랜덤 숫자 10개 가진 리스트 만들기 (랜덤 값 범위: 1~100)

mylist4 = [random.randint(1,100) for i in range(10)]

print(mylist4)
