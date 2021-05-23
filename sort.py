# 버블 정렬 구현 및 사용 예제 
#-------------------------------------------------------
# 버블 정렬 함수                        
#  전달 인수:                           
#    list = 정수형 배열                 
#    cnt = 배열의 요소 개수             
#  반환값: -1 = 정렬 안함, 0 = 정상 수행
def bubble_sort(list_data):
  cnt = len(test_list)   
  # 원소 개수가 2개 미만이면 정렬 불필요 */
  if cnt < 2:
    return -1

  for i in range(cnt, -1, -1): 
    for j in range(0, i - 1):
      if list_data[j] > list_data[j + 1]:
        temp = list_data[j]
        list_data[j] = list_data[j + 1]
        list_data[j + 1] = temp
        
  return 0

#-------------------------------------------------------
# 메인 처리 시작

test_list = [5, 8, 10, -1, -10, 100, 50, 90, 45, 64, 7,
             9, -20, -10, -1, 0, 255, 500, -300, -256]

# 원래 자료 출력 
print(test_list)

print("\nBubble sorting...\n")

# 버블 정렬 함수 호출 
bubble_sort(test_list)

# 정렬된 자료 출력 
print(test_list)

