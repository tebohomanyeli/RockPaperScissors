from random import randint
#Pictures(SQR) of the rock paper and scissors
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

#converting the options into a list:
game_list   = [rock , paper , scissors] 

#Prompt Input and print relevant picture
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n enter:  "))

if   user_choice == 0:
    print(game_list[user_choice])
elif user_choice == 1:
    print(game_list[user_choice])
elif user_choice == 2:
    print(game_list[user_choice])
else:
    print("Sorry this is not a valid move.")

#Randomly choosing the computer's move.
comp_choice = randint(0,2)
print("\n\nComputer chose:") ; print(game_list[comp_choice])


#Conditions and Rules of the game:
if  user_choice == 0:                   #Rock
    if comp_choice == 0:
        print("You Draw")
    elif comp_choice == 1:
        print("You Lose")
    elif comp_choice == 2:
        print("You Win")

elif user_choice == 1:                  #Paper
    if comp_choice == 0:
        print("You Win")
    elif comp_choice == 1:
        print("You Draw")
    elif comp_choice == 2:
        print("You Lose")

elif user_choice == 2:                  #Scissors
    if comp_choice == 0:
        print("You Lose")
    elif comp_choice == 1:
        print("You Win")
    elif comp_choice == 2:
        print("You Draw")




