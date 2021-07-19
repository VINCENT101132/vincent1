"""
輸入一數字n為尋找的區間範圍, 找出區間範圍
的質數顯示在螢幕上，其餘不顯示。
​
​
"""

n=int(input("請輸入整數"))
b=0
if n>1:
  print(2)
  for i in range(3,n+1):
    for j in range(2,i):
      if i%j==0:
        b=1
        break
      else:
        b=0
    if b==0:
      print(i)