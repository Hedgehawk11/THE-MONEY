import os
import time as t
import random as r
import sys as sus
food=50
x = 99**499
cash = 15
worker = r.randint(1, 1000)
is_boosted = False
bills = r.randint(1, 2)
nobill = False

print('THE MONEY(now with stock)')
while True:
  print("food levels are ",food)
  food-=1
  print('you have $' + str(cash))
  choice1 = input('\033[34minvest/upgrades/work/lottery/donate/buy/cheat/ \033[37m \n')

  if choice1 == 'invest':
        while True:
            choice2 = int(input('how much MONEY do you want to invest '))
            if choice2 <= cash:
                break
        cash -= choice2
        t.sleep(5)
        crash = r.randint(1, 10)
        if crash == 2:
            choice2 *= 5
            print('\u001b[31m \n you lost', choice2, 'bucks\u001b[37m ')
            if is_boosted:
                cash = float(cash)
                cash += choice2 / 2
                cash = round(cash)
                cash = int(cash)
                print('you got half back')
        else:
            cash += choice2 * 3

  if choice1 == 'upgrades':
        choice2 = input(
            'what do you want to buy \n \u001b[36m work more $1000 \n \u001b[35m insurance $1,000,000 BUY THIS ONE TIME \u001b[37m \n'
        )
        if choice2 == 'work more':
            worker += 10
            cash -= 1000
        if choice2 == 'insurance':
            print('ok')
            cash -= 1000000
            is_boosted = True

  if choice1 == 'work':
        t.sleep(10)
        cash += worker
        print('you worked and got money')

  if choice1 == 'lottery':
        cash -= 5
        if r.randint(1, 1000) == 1:
            print('we have a winner')
            cash += r.randint(1000000, 10000000000)
        else:
            print('\u001b[31m you wasted 5 bucks\u001b[37m ')

  if choice1 == 'donate':
        choice2 = input(
            'would you like to donate to charity or donate to animal shelter? \n'
        )
        if choice2 == 'charity':
            trix = r.randint(1, 10)
            amount = int(input('How much money would you like to donate? \n'))
            cash -= amount
            if trix <= 4:
                t.sleep(4)
                cash *= amount
                print(
                    'Since you gave to charity, charity gave back twice the money you donated to them! \n'
                )
        elif choice2 == 'animal shelter':
            trix = r.randint(1, 10)
            if trix <= 4:
                print('Oh no! A Lion stole your money')
                cash = 1
            else:
                print(
                    'You scared the money thief lion. The Animal Shelter payed you for donating to them. \n'
                )
                cash += 1000

  if choice1 == "buy":
        y = input("where would you like to shop food/de mart\n")
        if y == "food":
            fud = input(
                "hello welcome to food mart \n  pizza $7  \n burger $5 \n fries $2 \n sprite $1"
            )
            if fud == "pizza":
                pizza = int(input("how many pizza do you wanna buy"))
                print('successfully bought pizza')
                cash -= 7 * pizza
            elif fud == "burger":
                burger = int(input("how many burgers do you wanna get\n"))
                print('successfully bought burger(s)')
                cash -= 5 * burger
            elif fud == "fries":
                discount = r.randint(1, 10)
                if discount <= 8:
                    fries = int(input("How many fries you want?"))
                    print('Successfully bought fries.')
                    cash -= 2 * fries
                elif discount <= 10:
                    print('You got free fries! Discount, woo!')
            elif fud == "sprite":
                print(
                    'box of sprite $12 \n normal sprite can $1\n plastic sprite bottle $3 \n big sprite bottle (party size) $11\n'
                )
                q = input("choose")
                if q == "box of sprite":
                    cash -= 12
                    ('bought box of cans (sprite)')
                elif q == "normal sprite can" or q == "sprite can":
                    sprite = int(input('how many sprite cans you want?\n'))
                    cash -= 1 * sprite
                    print('successfuly bought')
                elif q == "big sprite bottle":
                  sprite = int(input('How many big bottles do you want? \n'))
                  cash -= 11 * sprite
                  print ('successfully bought the party size sprite bottle \n')
                elif q == "plastic sprite bottle":
                  cash -= 3
                  print ('Successfully bought')
        elif y == 'de mart':
          print ('De Mart is currently under construction, sorry.')
          
          
          

  if choice1 == 'cheat':
        print('enter cheat code')
        cheat = input()
        my_secret = os.environ['cheat1']
        if cheat == my_secret:
            print('money added')
            cash += 1000000000000000
        my_secret = os.environ['cheat2']
        if cheat == my_secret:
            sus.exit('your broke')
        my_secret = os.environ['cheat3']
        if cheat == my_secret:
            cash = cash * 3
        my_secret = os.environ['cheat4']
        if cheat == my_secret:
            cash += r.randint(1000000, 10000000000)
        my_secret = os.environ['cheat5']
        if cheat == my_secret:
            cash += 69420
        my_secret = os.environ['cheat6']
        if cheat == my_secret:
            cash += 1000000
        my_secret = os.environ['cheat7']
        if cheat == my_secret:
            cash = cash / 2
        my_secret = os.environ['cheat8']
        if cheat == my_secret:
            nobill = True
        my_secret = os.environ['cheat9']
        if cheat == my_secret:
          print('hi')


  if bills == 2 and not nobill:
        w = input('You need to pay your bills. Will you? ')
        if 2 != "yes" or w != '':
          cash = 0
          print('You did not pay your bills and the IRS took your money. and you died unexpectedly')
          sus.exit("PAY.YOUR.BILLS.")
        else:
          vary = r.randint(1, 10)
          if vary <= 9:
            cash -= 10
          elif vary <= 10:
            cash -= 15

  if cash <= 0:
      sus.exit("you're broke and died")
  if food <= 0:
        sus.exit ("you died of hunger...")
  