"""
Topic:華氏溫度轉攝氏溫度
​
Show:Please input Celsius Temperature:
Input:60
Output:
60.0F = 15.6C
​
"""

t=int(input('請輸入溫度(F)'))
T=str((t-32)/9*5)
print(T+'C')