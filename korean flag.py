# 태극기 그리는 파이썬 그래픽 예제
# korean flag.py
# ver 1.0  by jongho won
# ver 2.0  by sangmoon oh 

import turtle as t
import math as m

width = 1200            # 태극기 밑변 (높이의 3/2)
height = 800            # 태극기 높이 (밑변의 2/3)
diameter = height / 2   # 태극원 지름 = 높이 / 2
radius = height / 4     # 태극원 반지름 = 높이 / 4

# 대각선 길이 구하기 (= 1432)
diagonal_length = m.sqrt(width*width + height*height)
# 대각선 각도 구하기 (= 33.69도)
diagonal_degree = m.atan2(height,width) * 180/m.pi

t.title("Korean Flag")  # 그래픽 창 제목 지정
t.setup(width, height)  # 그래픽 창 크기 지정
t.bgcolor("white")      # 배경색 지정

# 괘의 한 선 그리기 
def draw_k():
    n = [radius/2,radius/6,radius,radius/6,radius/2]
    t.pendown()
    t.color("black", "black")
    t.begin_fill()
    for size in n:
        t.left(90)
        t.forward(size)
    t.end_fill()
    t.penup()

# 괘 한 선의 중간을 흰색으로 그리기 (분리된 괘)
def draw_k_white():
    n = [radius/24+1,radius/6+2,radius/12+2,radius/6+2,radius/24+1] 
    t.color("white", "white")
    t.begin_fill()
    t.right(90)
    t.forward(1)
    for size in n:
        t.left(90)
        t.forward(size)
    t.end_fill()    

# 건괘 그리기 
def draw_gun():
    for r in range(20, 27, 3):
        t.home()     
        t.right(diagonal_degree+180)
        t.forward(radius*r/12)
        draw_k()

# 리괘 그리기
def draw_ri():
    for r in range(20, 27, 3):
        t.home()     
        t.right(-diagonal_degree+180)
        t.forward(radius*r/12)
        draw_k()
        if( r == 23 ):
            draw_k_white()

# 감괘 그리기
def draw_kam():
    for r in range(20, 27, 3):
        t.home()     
        t.left(diagonal_degree)
        t.forward(radius*r/12)
        draw_k()
        if( r != 23 ):
            draw_k_white()

# 곤괘 그리기
def draw_kon():
    for r in range(20, 27, 3):
        t.home()     
        t.left(-diagonal_degree)
        t.forward(radius*r/12)
        draw_k()
        draw_k_white()

# 4괘 모두 그리기 
def draw_4k():
    t.penup()    
    draw_gun()  # 건
    draw_ri()   # 리
    draw_kam()  # 감
    draw_kon()  # 곤  

# 태극 원형 모양 그리기
def draw_taegeuk():
    t.home()
    t.right(diagonal_degree)
    t.forward(radius)
    t.left(90)
    t.color("#C60C30", "#C60C30")  # 붉은색
    t.begin_fill()
    t.circle(radius, 180)
    t.end_fill()
    t.color("#003478", "#003478")  # 청색
    t.begin_fill()
    t.circle(radius, 180)
    t.end_fill()
    t.home()
    t.left(90 - diagonal_degree)
    t.begin_fill()
    t.color("#C60C30", "#C60C30")  # 붉은색
    t.circle(radius / 2)
    t.end_fill()
    t.home()
    t.right(90 + diagonal_degree)
    t.begin_fill()
    t.color("#003478", "#003478")  # 청색
    t.circle(radius / 2)
    t.end_fill()

#---------------------------------------------
# 메인 처리 
#---------------------------------------------

t.speed(0)

# 태극 모양 그리기 
draw_taegeuk()

# 4괘 그리기
draw_4k()

# 거북이 커서 숨김
t.hideturtle()  
