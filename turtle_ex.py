# turtle graphic
import turtle
from turtle import Turtle

myt = Turtle()   # 객체 생성 

def square():
  for side in range(4):
    turtle.forward(60)
    turtle.left(90)

def polygon(sides, length, angle):
    for s in range(sides):
        turtle.forward(length)
        turtle.left(angle)

def flower(petal_sides, petal_angle, poly_sides, poly_length, poly_angle):
    for s in range(petal_sides):
        polygon(poly_sides, poly_length, poly_angle)
        turtle.left(petal_angle)
        
turtle.clear()  # 화면 정리
turtle.reset()  # 원래 위치로 & 화면 정리 

for i in range(4):
  turtle.forward(200)
  turtle.left(90)

myt.color('red')
myt.goto(300, 300)
#print (myt.position())

polygon(8, 30, 150)

myt.penup()
myt.setposition((60, 0))
myt.pendown()

target = Turtle()
target.forward(50)

target_coords = target.position()
new_heading = myt.towards(target_coords)
myt.setheading(new_heading)
myt.forward(50)


 
