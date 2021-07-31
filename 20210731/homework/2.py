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
  print("獲得{}的$,目前的${}".format(get_money,st[2]))
  return st

def fight(st):
  monster_life=random.randint(2,10)
  print('遇到怪物了,hp{}'.format(monster_life))
  while True:
    time.sleep(1)
    attack=random.randint(1,3)
    monster_life-=attack
    print('造成{}的傷害,怪物hp{}'.format(attack,monster_life))
    if monster_life<=0:
      get_money=random.randint(10,20)
      st[2]+=get_money
      print('已擊敗怪物,獲得{}的$,玩家狀態{}'.format(get_money,st))
      break
    time.sleep(1)
    st[1]-=1
    print('玩家hp{}'.format(st[1]))
    if st[1]<=0:
      st[0]=0
      break
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