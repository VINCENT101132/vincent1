"""
Topic:請使用input輸入要印制的箭頭大小
可利用字串乘法
e.g.
val="*" * 3
print(val)
***
​
​
1.Show:Please in row: 
2.input:3
  *  
 *** 
*****
  *  
  *  
  * 
"""

val=int(input())
for a in range(val):
  print(' '*(val-a)+'*'*(a+a+1))
for b in range(val):
  print(' '*val+'*')