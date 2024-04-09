rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
print("Welcome to Rock Paper Scissors Game\n")
chose = int(input("Choose 1 for Rock, 2 for Paper and 3 for Scissors!\n"))
import random
computer = random.randint(1, 3)

if chose == 1:
  print(f"You:Rock\n {rock}")
elif chose == 2:
  print (f"You:Paper\n {paper}")
else:
  print(f"You:Scissors\n {scissors}")

if computer == 1:
  print(f"Computer:Rock\n {rock}")
elif computer == 2:
  print (f"Computer:Paper\n {paper}")
else:
  print(f"Computer:Scissors\n {scissors}")

if chose == 1 and computer == 1:
  print("Draw")
elif chose == 1 and computer == 2:
  print("You lose")
elif chose == 1 and computer == 3:
  print("You win")
elif chose == 2 and computer == 1:
  print("You win")
elif chose == 2 and computer == 2:
  print("Draw")
elif chose == 2 and computer == 3:
  print("You lose")
elif chose == 3 and computer == 1:
  print("You lose")
elif chose == 3 and computer == 2:
  print("You win")
else:
  print("Draw")
