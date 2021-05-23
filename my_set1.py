my_set = {1,2,3,4,5,4,3,2,1}
print(my_set)

my_dic = {'국어':90, '영어':95, '수학':90}   # 사전 자료 생성 
my_set = set(my_dic)    # 셋 자료 생성 
print(my_dic)
print(my_set)
my_set = set(my_dic.values())    # 셋 자료 생성 
print(my_set)

# set 자료 생성하기
my_set1 = set()       # 요소가 없는 set 자료 생성 
my_set2 = {1, 2, 3}   # 요소가 있는 set 자료 생성
print(my_set1)
print(my_set2)

# in을 이용한 검색 
if 1 in my_set2: 
  print("자료가 존재합니다.")
else:
  print("자료가 존재하지 않습니다.")
