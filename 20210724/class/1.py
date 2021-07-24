j=[]
while True:
  print('1. 想加入菜單的果汁')
  print('2. 顯示目前所有果汁')
  print('3. 離開系統')
  a=input('請選擇功能')
  if  a=='1':
    c=input('想輸入的果汁?')
    '''for i in j:
      if i==c:
        print('已經有了')
        break
    else:
      j.append(c)
      print('已新增')'''
    if c in j:
      print('已經有了')
    else:
      j.append(c)
      print('已新增')
  elif a=='2':
    print(j)
  elif a=='3':
    break
