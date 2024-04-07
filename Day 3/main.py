#This program is created as a "Choose your Ownn Fortune" game ENJOY!!!

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

quest1 = input("You are in a cross road and you have two chooses, choose between left and right\n")
quest1 = quest1.lower()
if quest1 == "left":
  quest2 = input("YOu arrived in front of a river, choose whether to swim or wait\n")
  quest2 = quest2.lower()
  if quest2 == "wait":
    quest3 = input("Three boats having diffrent colours eventually arrived, which colour you will ride in: Red or Yellow or Blue\n")
    quest3 = quest3.lower()
    if quest3 == "yellow":
      print("You got home safe!\nYou win!")
    elif quest3 == "red":
      print("Your boat exploded midway!\nGame Over!")
    elif quest3 == "blue":
      print("You got eaten by sharkers!\nGame Over!")
    else:
      print("Game Over!")
  elif quest2 == "swim":
    print("You got eaten by sharkers!\nGame Over!")
  else:
    print("Game Over!")
elif quest1 == "right":
  print("You fell into a hole!\nGame Over!")
else:
  print("Game Over!")
  
