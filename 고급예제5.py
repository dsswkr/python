# 고급 예제 5
# 콘솔창에서 실행하는 예제입니다.
# python 고급예제5.py <엔터>

import os

MAZE_SIZE = 12
WALL = '#'
MOUSE = 'Q'
END = '$'
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

Exit = False 
ms = [0, 0, 0]      # 마우스 좌표와 방향 저장 x, y, d
old_ms = [0, 0, 0]  # 마우스 이전 좌표와 방향 저장

# 미로 정의 데이터
maze = [
  ['#','#','#','#','#','#','#','#','#','#','#','#'],
  ['#',' ',' ',' ',' ','#','#',' ',' ',' ',' ','#'],
  ['#',' ','#','#',' ','#','#',' ','#','#',' ','#'],
  ['#',' ','#','#',' ','#','#',' ',' ','#',' ','#'],
  ['#',' ','#','#',' ','#','#','#',' ','#',' ','#'],
  ['#',' ','#','#',' ',' ','#','#',' ','#',' ','#'],
  ['#',' ','#','#','#',' ','#','#',' ','#',' ','#'],
  ['#',' ','#',' ',' ',' ','#','#',' ','#',' ','#'],
  ['#',' ','#',' ','#','#','#','#',' ','#',' ','#'],
  ['#',' ','#',' ','#','#','#','#',' ','#',' ','#'],
  ['#',' ','#',' ',' ',' ',' ',' ',' ','#',' ','#'],
  ['#','#','#','#','#','#','#','#','#','#','$','#']]

# 미로의 x, y 위치에 있는 값 읽기 
def get_mazexy(x, y):
  if (ms[0] < 0 or ms[0] > MAZE_SIZE-1 or ms[1] < 0 or ms[1] > MAZE_SIZE-1):
    print("[get_mazexy()] Mouse-position error!!!")    
    return None
  else:
    return maze[y][x]

# 미로의 x, y 위치에 값 저장하기 
def set_mazexy(x, y, c):
  if (ms[0] < 0 or ms[0] > MAZE_SIZE-1 or ms[1] < 0 or ms[1] > MAZE_SIZE-1):
    print("[set_mazexy()] Mouse-position error!!!")    
    return None
  else:
    maze[y][x] = str(c)

# 화면 갱신하기 
def draw(x, y):
  set_mazexy(old_ms[0], old_ms[1], ' ');
  old_ms[0] = x
  old_ms[1] = y
  set_mazexy(x, y, MOUSE);
  os.system("cls");   # 화면 지우기
  for i in range(MAZE_SIZE):
    print("".join(maze[i]))

# 오른쪽으로 돌기 
def turn_right():
  ms[2]= (ms[2]+1) % 4

# 왼쪽으로 돌기
def turn_left():
  ms[2] = 3 if ms[2] == 0 else ms[2]-1

# 현재 방향으로 마우스 좌표 이동하기 
def go():
  if ms[2] == UP:
    ms[1] += 1
  elif ms[2] == DOWN:
    ms[1] -= 1    
  elif ms[2] == RIGHT:
    ms[0] += 1
  elif ms[2] == LEFT:
    ms[0] -= 1
  
  if ms[0] < 0 or ms[0] > MAZE_SIZE or ms[1] < 0 or ms[1] > MAZE_SIZE:
    print("[ERROR] Mouse-position error!!!");
    return False

  if get_mazexy(ms[0], ms[1]) == END:
    return True
  else: 
    return False

# 이동 방향 쪽에 벽이 있는지 검사 
def wall_ahead():
  if ms[2] == UP:   
    if get_mazexy(ms[0], ms[1]+1) == WALL:
      return True    
  elif ms[2] == DOWN: 
    if get_mazexy(ms[0], ms[1]-1) == WALL:
      return True  
  elif ms[2] == RIGHT:    
    if get_mazexy(ms[0]+1, ms[1]) == WALL:
      return True      
  elif ms[2] == LEFT: 
    if get_mazexy(ms[0]-1, ms[1]) == WALL:
      return True    
  return False;

#--------------------------------------------------------------------
# 메인 처리 

old_ms[0] = ms[0] = 1     # x 
old_ms[1] = ms[1] = 10;   # y
ms[2] = UP                # 방향

while True:  	          # 탈출하기 전까지 반복
  # 화면 갱신
  draw(ms[0], ms[1])

  if Exit == True:
    break

  turn_right()     	  # 오른쪽으로 돌기 
  while wall_ahead() == True:   # 앞에 벽이 없을 때까지 왼쪽으로 돌기 
    turn_left()

  print("\nMouse: %d, %d" %(ms[0], ms[1]))
  Exit = go()             # 벽이 없는 방향으로 이동 

print("\n 성공!!")        # 성공 메시지를 출력하고 키 입력 대기

