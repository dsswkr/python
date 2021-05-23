a_set = { 1, 2, 3, 4, 5 }
b_set = { 4, 5, 6, 7, 8 }

# 교집합: & 연산자 또는 intersection() 함수 사용 
print( a_set & b_set )    # a_set.intersection(b_set)

# 합집합: | 연산자 또는 union() 함수 사용 
print( a_set | b_set )   # a_set.union(b_set)

# 차집합: - 연산자 
print( a_set - b_set )

# 대칭차집합(합집합-교집합): ^ 연산자 
print( a_set ^ b_set )
