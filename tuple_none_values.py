# 튜플 만들기
import random

# None 값을 10개 가진 튜플 만들기
mytuple1 = ([None] * 10)

print(mytuple1)


# 10개 항목의 값이 0인 리스트 만들기 
mytuple2 = ([0] * 10)

print(mytuple2)

# 연속된 값을 10개 가진 리스트 만들기 (예: 1~10)
mytuple3 = ([i for i in range(1, 11)])

print(mytuple3)

# 랜덤 숫자 10개 가진 리스트 만들기 (랜덤 값 범위: 1~100)

mytuple4 = ([random.randint(1,100) for i in range(10)])

print(mytuple4)
