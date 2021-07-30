'''
使用者輸入兩個數num1 and num2，
並使用function def 求最小公倍數
value = lcm(num1, num2)
'''

def lcm(x, y):
   if x > y:
       largest = x
   else:
       largest = y
   while(True):
       if((largest % x == 0) and (largest % y == 0)):
           lcm = largest
           break
       largest += 1
   return lcm
num1 = int(input("輸入整數"))
num2 = int(input("輸入整數"))
print(lcm(num1, num2))