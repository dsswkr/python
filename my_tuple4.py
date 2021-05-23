my_tuple = ( '사과', '배', '바나나', '감', '포도' )

new_tuple = my_tuple + ('딸기',)   # OK
# new_tuple = my_tuple + ('딸기')  # ('딸기')는 문자열 에러

print(my_tuple)
print(new_tuple)

