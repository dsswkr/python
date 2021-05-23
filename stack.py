# 리스트를 이용한 stack 자료 구조 

# 스택 생성
my_stack = []

# 스택 푸시(넣기) 함수 
def push_stack( v ):
  my_stack.append(v)
  return v

# 스택 팝(꺼내기) 함수 
def pop_stack():
  if(len(my_stack) > 0):  
    return my_stack.pop()
  else:
    return None

# 스택 자료 출력 
def print_stack():
  print("STACK: " + str(my_stack))

#---------------------------------------
# 메인 처리 

print("PUSH > " + str(push_stack(1)))
print("PUSH > " + str(push_stack(2)))
print("PUSH > " + str(push_stack(3)))
print("PUSH > " + str(push_stack(4)))
print("PUSH > " + str(push_stack(5)))
print_stack()

print("POP > " + str(pop_stack()))
print("POP > " + str(pop_stack()))
print("POP > " + str(pop_stack()))
print("POP > " + str(pop_stack()))
print("POP > " + str(pop_stack()))
print("POP > " + str(pop_stack()))
print_stack()
