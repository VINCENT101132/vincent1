while True:
  a=input()
  b=input()
  try:
    print('a/b='+str(float(a)/float(b)))
    break
  except:
    print('請輸入數字')