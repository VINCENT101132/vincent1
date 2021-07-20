import random
n=int(input())
b=random.randint(1,n)
for a in range(1,n+1):
  if a!=b:
    continue
  print(a)