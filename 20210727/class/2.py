def add(j):
  A=[]
  A=j
  c=input('想輸入的果汁?')
  if c in j:
    print('已經有了')
  else:
    A.append(c)
    print('已新增')
  return A

def show(j):
  b=[]
  print(j)
  b=j
  return b

def remove(j):
  e=[]
  e=j
  c=input('想刪除的果汁?')
  if c in j:
    e.remove(c)
    print('已刪除')
  else:
    print('無此果汁')
  return e

j=[]
w=[add,show,remove]
while True:
  print('1. 想加入菜單的果汁')
  print('2. 顯示目前所有果汁')
  print('3. 刪除菜單上的果汁')
  print('4. 離開系統')
  a=int(input('請選擇功能'))
  if a==4:
    break
  else:
    j=w[a-1](j)