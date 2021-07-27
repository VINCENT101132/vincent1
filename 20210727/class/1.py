import random

def who_is_winner(usr_list,cmp_list):
  cmp_sc=sum(cmp_list)
  usr_sc=sum(usr_list)

  print('user score %d' % usr_sc)
  print('computer score %d' % cmp_sc)

  if usr_sc>cmp_sc:
    print('user is winner')
  elif cmp_sc>usr_sc:
    print('computer is winner')
  else:
    print('tie')

def roll_dice(n):
  dice=[]
  for i in range(n):
    dice.append(random.randint(1,6))
  return dice

num_dice=int(input('輸入骰子數'))
user=roll_dice(num_dice)
comp=roll_dice(num_dice)
who_is_winner(user,comp)