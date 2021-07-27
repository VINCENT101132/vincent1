import random
def roll_dice(n):
  dice=[]
  for i in range(n):
    dice.append(random.randint(1,6))
  return dice
num_dice=int(input('輸入骰子數'))
print(roll_dice(num_dice))