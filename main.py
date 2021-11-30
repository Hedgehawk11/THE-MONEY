import os
import time as t
import random as r
import sys as sus

cash = 5



print ('THE MONEY(now with stock)\n')
t.sleep(5)
while True:
  print('you have $'+str(cash))
  choice1 = input('invest/spend/get more/cheat ')
  if choice1 == 'invest':
    choice2 = int(input('how much MONEY do you want to invest '))
    cash -= choice2
    t.sleep(5)
    crash = r.randint(1,2)
    if crash == 2:
      print('you lost',choice2,'bucks')
    else:
      cash += choice2 * 3
    
  if choice1 == 'spend':
    choice2 = input('how much do you want to spend')
    cash -= choice2

  if cash <= 0:
    break