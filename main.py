'''import random
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
  monster_life=random.randint(10,30)
  print('遇到怪物了,hp{}'.format(monster_life))
  while True:
    time.sleep(1)
    a=input('是否使用魔法攻擊(回答yes or no)')
    if a=='yes':
      if st[3]>=1:
        magic_attack=random.randint(4,10)
        monster_life-=magic_attack
        print('造成{}的傷害,怪物hp{}'.format(magic_attack,monster_life))
        st[3]-=1
      else:
        print('你魔力不足,哈哈哈這回合你不能打了')
    elif a=='no':
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

def store(st):
  add_life=5
  add_magic=5
  print('1. 回血藥水 100$')
  print('2. 回魔藥水 300$')
  print('3. 小孩子才做選擇,我全都要')
  print('4. 我只是路過')
  print('5. 我要挑武器啦啦啦啦啦啦')
  a=int(input('請選擇商品'))
  if a==1:
    if st[2]>=100:
      print('你已購買回血藥水')
      st[1]+=add_life
      st[2]-=100
    else:
      print('滾吧,窮光蛋')
      return st
  elif a==2:
    if st[2]>=300:
      print('你已購買回魔藥水')
      st[3]+=add_magic
      st[2]-=300
    else:
      print('滾吧,窮光蛋')
      return st
  elif a==3:
    if st[2]>=400:
      print('你已購買回血藥水和回魔藥水')
      st[1]+=add_life
      st[3]+=add_magic
      st[2]-=400
    else:
      print('滾吧,窮光蛋')
  elif a==4:
    print('byebye')
  elif a==5:
    if st[4]<5:
      print('1.小刀  50$')
      print('2.長弓  300$')
      print('3.魔杖  500$')
      print('4.武器詳情')
      b=int(input('請選擇商品'))
      if b==1:
        if st[2]>=50:
          print('你已購買小刀')
          st[1]+=add_life
          st[2]-=100
        else:
          print('滾吧,窮光蛋')
          return st
      elif b==2:
        if st[2]>=300:
          print('你已購買回魔藥水')
          st[3]+=add_magic
          st[2]-=300
        else:
          print('滾吧,窮光蛋')
          return st
      elif b==3:
        if st[2]>=400:
          print('你已購買回血藥水和回魔藥水')
          st[1]+=add_life
          st[3]+=add_magic
          st[2]-=400
        else:
          print('滾吧,窮光蛋')
    else:
      print('裝備欄已達上限')    
  return st       


st=[1,10,1000,10,0,0]
game=[udput_life,udput_money,fight,store]
while True:
  case=random.randrange(0,len(game))
  st=game[case](st)
  time.sleep(1)
  print('玩家狀態{}'.format(st))
  if st[0]==0:
    print('Game Over')
    break'''

for a in range(5):
  print(' '*(4-a)+'*'*(a+1))