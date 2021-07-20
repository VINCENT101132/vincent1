import random
r=random.randint(1,100)
c=1
d=100
while True:
  b=int(input('請輸入數字'))
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