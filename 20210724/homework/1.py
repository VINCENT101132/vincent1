'''
str = "00000:00000:00000:00000:00000"
請使用list 分割及重組元素
for loop show list value
"99999:00000:00000:00000:00000"  第一圈
"00000:99999:00000:00000:00000"  第二圈
"00000:00000:99999:00000:00000"  第三圈
"00000:00000:00000:99999:00000"  第四圈
"00000:00000:00000:00000:99999"  第五圈
只能用一個list個
'''


for c in range(5):
  a=['00000','00000','00000','00000','00000']
  a.remove('00000')
  a.insert(c,'99999')
  print(a)