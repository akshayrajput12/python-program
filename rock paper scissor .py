#rock wins aginst scissors
#scissors wins aginst paper
#paper wins aginst rock
#0-rock
#1-paper
#2-scissors

#user case

print("0 is for Rock")
print("1 is for paper")
print("2 is for scissors")

rock = '🪨'
paper = "📃"
scissors = '✂'
gameIcons = [rock, paper, scissors]

import random

i = "yes"
while i == "yes":

  user_choice = int(input("Enter your   choice: "))

  if user_choice >= 3 or user_choice < 0:
    print("Invalid output")
  else:
    print(gameIcons[user_choice])
    computer_choice = random.randint(0, 2)
    print("computer choice:")
    print(computer_choice)
    print(gameIcons[computer_choice])
    if computer_choice == user_choice:
      print("its a draw.")
    elif computer_choice == 0 and user_choice == 2:
      print("You loose")
    elif user_choice == 0 and computer_choice == 2:
      print("You win")
    elif computer_choice > user_choice:
      print("You loose")
    elif user_choice > computer_choice:
      print("You win")
  i = input("Want to play again: yes/no  ::")
