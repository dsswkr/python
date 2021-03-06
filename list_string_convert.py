# 파이썬 내장함수를 이용해 문자열을 리스트로 또는 반대로 변환할 수 있습니다. 
# Join 함수는 리스트를 특정 구분자를 포함해 문자열로 변환합니다. 
# Split함수는 문자열을 특정 구분자로 나누어 리스트로 변환합니다.


# (1) 리스트를 문자열로 변환하기

# 리스트 lst
lst = ['국어', '수학', '정보', '영어', '체육']

# 쉼표로 구분하여 문자열로 결합하기 
s = ",".join(lst)

print(s)  # >> 국어,수학,정보,영어,체육 

#출력할 때 한 줄에 한 문자열로 출력하기
print("\n".join(lst))
# 국어
# 수학 
# 정보 
# 영어
# 체육



# (2) 문자열을 리스트로 변환하기

# 문자열 s 내용을 쉼표 구분자로 나눠서 리스트에 저장하기
new_lst = s.split(",")   
print(new_lst)   # >> ['국어', '수학', '정보', '영어', '체육']
