import random
import time 
from replit import clear
ppoint = 0
epoint = 0
W = '\033[1;37m'
O = '\033[0m'


print('''{}__            _____
\ \        /\|  __  \ 
 \ \  /\  /  \ |__) |
  \ \/  \/ /\ \ __  / 
   \  /\  ____ \  \ \ 
    \/  \/    \_\  \_\{} by Dart#5588 / Zexogon
'''.format(W, O))
print('''welcome to war

press enter to begin

or type rules if you dont know them''')
y = input(">")
clear()
if y == "rules":
  print('''how to play:
  you are given a card with a number 1 - 14
  
  if you think your card is larger then play
  
  if it is then you get a point!
  
  if it isnt then the enemy gets a point
  
  if you choose not to play and you would have lost then no one gets a point
  
  if you choose not to play and you would have won the enemy gets a point
  
  play until you reach the winning amount of points
  
  press enter to continue''')
  input()
  clear()
rpoint = int(input("how many points to win the round?\n>"))
clear()
while True:
  cardp = random.randint(1,14) #chooses the cards
  carde = random.randint(1,14)
  
  print("your card:", cardp)
  print('''
  play?   (y/n)''')
  x = input(">")
  clear()
  if x != "y" and x != "n":
    print("no input, you lost a point") #if you dont answer weather or not you want to play to prevent cheating
    if ppoint != 0:
      ppoint = ppoint - 1
  if x == "y":
    if cardp >= carde:
      print("you won!")
      ppoint = ppoint + 1
    else:
      print("you lost")
      epoint = epoint + 1
  if x == "n":
    if cardp >= carde:
      print("you would have won! enemy gains a point")
      epoint = epoint + 1
    else:
      print("good call, no points")
  print("")
  print("enemies card:", carde)
  print("")
  print("your points:", ppoint, "enemies points:", epoint)
  input()
  clear()
  if epoint == rpoint:
    print('''you lost the game
      
      press enter to play again
      ''')
    print("the final score:\n")
    print("your points:", ppoint, "enemies points:", epoint)
    epoint = 0
    ppoint = 0
    input()
    clear()
    continue
  if ppoint == rpoint:
    print('''you won the game!
    
    press enter to play again
    ''')
    print("the final score:\n")
    print("your points:", ppoint, "enemies points:", epoint)
    epoint = 0
    ppoint = 0
    input()
    clear()
    continue