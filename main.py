j=['apple','ball','car']
print(j)
while True:
  c=input('請輸入單字')
  if c in j:
    j.remove(c)
  else:
    j.append(c)
  print(j)
