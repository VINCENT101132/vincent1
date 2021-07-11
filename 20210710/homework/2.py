"""
Topic:輸入三角形三邊，判斷是否能構成三角形，
　　　是三角形則顯示面積和周長，不行則顯示，無法構成三角形:
​
Triangle Area formula: 
p = 1/2 (a+b+c)
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
​
e.g.
Show:a ="
Input1:3
​
Show:b ="
Input2:4
​
Show:c ="
Input3:5
​
output:
perimeter: 12.000000
Area: 6.000000
"""

short=int(input('請輸入三角形最短邊'))
long=int(input('請輸入三角形最長邊'))
middle=int(input('請輸入剩下的三角形邊'))

if (short+middle)>long and long>middle>short>0:
  p = (short+middle+long)/2
  area =str( (p * (p - short) * (p - middle) * (p - long)) ** 0.5)
  print("周長="+str(p*2))
  print('面積='+area)
else:
  print('無法形成三角形')