import random
import time

def udput_life(st):
  get_life=random.randint(1,3)
  st[1]+=get_life
  print("獲得{}的hp,目前的hp{}".format(get_life,st[1]))
  return st

def udput_money(st):
  get_money=random.randint(10,30)
  st[2]+=get_money
  print("獲得{}的$,目前的${}".format(get_life,st[2]))
  return st

def fight(st):
  return st

st=[1,10,0]
game=[udput_life,udput_money,fight]
while True:
  case=random.randrange(0,len(game))
  st=game[case](st)
  time.sleep(1)
  print('玩家狀態{}'.format(st))
  if st[0]==0:
    print('Game Over')
    break