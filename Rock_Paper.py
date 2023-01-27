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

#Write your code below this line 👇
choise = input("What do you choose, 0 for Rock, 1 for paper and 2 for Scissors: ")
game = [rock, paper, scissors]

user_choice = int(choise)
print(game[user_choice])

print("Computer choose:")
comp_choice = random.randint(0,3)
print(game[comp_choice])

if user_choice == 0 and comp_choice == 2:
    print("You Won!")
elif user_choice == 1 and comp_choice == 0:
    print("You Won!")
elif user_choice == 2 and comp_choice == 1:
    print("You Won!")
else:
    print("You Loose!")