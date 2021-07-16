"""
Topic:請使用turtle及loop及time.sleep(1)印出秒針動畫
​
e.g.
import time
time.sleep(1)
"""

import turtle
import time
for a in range(60):
  turtle.forward(50)
  turtle.home()
  time.sleep(1)
  turtle.clear()
  turtle.right(6*(a+1))