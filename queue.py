# 리스트를 이용한 queue 자료 구조 

# 큐 생성
my_queue = []

# 큐 넣기 함수 
def put_queue( v ):
  my_queue.append(v)
  return v

# 큐 꺼내기 함수 
def get_queue():
  if(len(my_queue) > 0):  
    return my_queue.pop(0)  # 0번째 요소
  else:
    return None

# 큐 자료 출력 
def print_queue():
  print("QUEUE: " + str(my_queue))

#---------------------------------------
# 메인 처리 

print("PUT > " + str(put_queue(1)))
print("PUT > " + str(put_queue(2)))
print("PUT > " + str(put_queue(3)))
print("PUT > " + str(put_queue(4)))
print("PUT > " + str(put_queue(5)))
print_queue()

print("GET > " + str(get_queue()))
print("GET > " + str(get_queue()))
print("GET > " + str(get_queue()))
print("GET > " + str(get_queue()))
print("GET > " + str(get_queue()))
print("GET > " + str(get_queue()))
print_queue()
