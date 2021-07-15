"""
Topic:請使用turtle及loop印出下列圖形
​
e.g.
turtle_stamp.jpg
可利用turtle.home()會回到原點(0.0)的特性
"""

import turtle
turtle.color('black')
turtle.shape('triangle')
turtle.penup()
for a in range(8):
  turtle.forward(70)
  turtle.stamp()
  turtle.home()
  turtle.right(45*(a+1))
turtle.stamp()