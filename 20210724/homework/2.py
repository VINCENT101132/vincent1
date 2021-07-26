'''
讓使用者輸入一個str，當str有在list裡面，就移除該str
沒有str就加入list, 並顯示最後的list，list初使值為
["apple", "ball" ,"car"]
'''

j=['apple','ball','car']
print(j)
while True:
  c=input('請輸入單字')
  if c in j:
    j.remove(c)
  else:
    j.append(c)
  print(j)