import turtle
import random

def leaves(x,y,color):
  turtle.penup()
  turtle.goto(x,y)
  turtle.pendown()
  turtle.setheading(0)
  turtle.color(color)
  turtle.begin_fill()   
  turtle.forward(40)
  turtle.left(120)
  turtle.forward(40)
  turtle.left(120)
  turtle.forward(40)  
  turtle.end_fill()

def trunk(x,y,color):
  turtle.penup()
  turtle.goto(x+12.5,y)
  turtle.pendown()
  turtle.color(color)
  turtle.setheading(0)
  turtle.begin_fill()
  turtle.forward(15)
  turtle.right(90)
  turtle.forward(25)
  turtle.right(90)
  turtle.forward(15)
  turtle.right(90)
  turtle.forward(25)
  turtle.end_fill()

def color():
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  color=(r/255,g/255,b/255)
  return color

times=int(input('請輸入次數'))
xy=200
for a in range(times):
  x=random.randint(-xy,xy)
  y=random.randint(-xy,xy)  
  leaves(x,y,color())
  trunk(x,y,color())