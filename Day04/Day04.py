import random

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
user = int(input("Let's play Rock, Paper or Scissors! Enter 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if user == 0:
  print("You chose Rock\n")
  print(rock)
elif user == 1:
  print("You chose Paper\n")
  print(paper)
else:
  print("You chose Scissors\n")
  print(scissors)

print("Computer's Turn: ")
game=[rock,paper,scissors]
computer = random.randint(0,2)
if(computer==0):
  print(game[0])
elif computer == 1:
  print(game[1])
else:
  print(game[2])

if(user == 1 and computer == 0):
  print("You Win!")
elif(user==1and computer ==2):
  print("You Lose!")
elif(user==0 and computer== 1):
  print("You Lose!")
elif(user==0 and computer== 2):
  print("You Win!")
elif(user==2 and computer== 0):
  print("You Lose!")
elif(user==2 and computer== 1):
  print("You Win!")
else:
  print("Sorry, it's a Draw")





