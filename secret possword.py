import random
r=random.randint(1,100)
c=1
d=100
for a in range(10):
  b=input('請輸入數字')
  try:
    b=int(b)
    if b>d or b< c:
      continue
    if b>r:
      d=b
      print('在({},{})之間'.format(c,d))
    elif b<r:
      c=b
      print('在({},{})之間'.format(c,d))
    else:
      print('猜中了')
      break
  except:
    print('不要亂輸入,您放棄了一次機會')
    continue
else:
  print("你輸了,正確答案是{}".format(r))