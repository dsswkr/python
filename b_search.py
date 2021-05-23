# a = 정수형 자료 리스트
# what = 찾으려는 값
# left = 왼쪽 검색 범위 
# right = 오른쪽 검색 범위
def b_search(data_list, what, left, right):
  if (right - left) < 2:
    if data_list[left] == what: 
      return left
    elif data_list[right] == what: 
      return right
    else: 
      return -1;  # 찾지 못함

  mid = int(left + (right - left) / 2)

  if data_list[mid] == what:
   return mid
  elif data_list[mid] > what:
    return b_search(data_list, what, left, mid - 1)
  else:   # data_list[mid] < what  
    return b_search(data_list, what, mid + 1, right)


# 정수형 배열에서 정수를 검색하는 함수   
# 전달인수                            	 
#   array = 정수형 자료 배열 이름		 
#   what = 찾으려는 정수 값 		
# 반환 값  				 
#   -1 = 찾지 못함                         
#   0 이상 = 검색 자료의 위치 (배열 인덱스 값) 
def search(data_list, what):
  return b_search(data_list, what, 0, len(data_list) - 1)

#--------------------------------------------------
# 메인 처리 

mylist = [i for i in range(100)]

ret = search(mylist, 99)
if ret == -1:
  print("찾을 수 없습니다.") 
else:
  print("%s, 위치는 mylist[%i]" %("찾음", ret)) 

ret = search(mylist, -1)
if ret == -1:
  print("찾을 수 없습니다.") 
else:
  print("%s, 위치는 mylist[%i]" %("찾음", ret)) 

ret = search(mylist, 0)
if ret == -1:
  print("찾을 수 없습니다.")  
else:
  print("%s, 위치는 mylist[%i]" %("찾음", ret)) 

