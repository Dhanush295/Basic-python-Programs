import random
# Welcome Screen
print("Welcome to the number guessing game! ")

# Randomly choosing the number
print("I'm thinking a number between 1 and 100. ")
guess = random.randint(1, 100)
print(guess)


start_game = True
e_life = 9
h_life = 4

# Comparing the values
def calculate(comp_guess, u_guess):
    if u_guess == comp_guess:
        return 0
    if u_guess > comp_guess:
        return 2
    if u_guess < comp_guess:
        return 1 


# Asking for difficulty level:
e_h = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
while start_game:
    user_guess = int(input("Make a guess: "))
    ans = calculate(guess, user_guess)
    if e_h == "easy":
        new_life =  e_life  
        if new_life == 0:
            print("You've run out of guess, you loose")
            start_game = False
        elif ans == 0:
            print(f"You got it!. The answer was {guess}")
            start_game = False
        elif ans == 2:
            print("Too high!")
            e_life += -1
            print(f"You have {new_life} attempts remaining to guess the number ")
        elif ans == 1:
            print("Too low!")
            e_life += -1
            print(f"You have {new_life} attempts remaining to guess the number ")

# For Harder level
    elif e_h == "hard":
        new_life = h_life  
        if new_life == 0:
            print("You've run out of guess, you loose")
            start_game = False
        elif ans == 0:
            print(f"You got it!. The answer was {guess}")
            start_game = False
        elif ans == 2:
            print("Too high!")
            h_life += -1
            print(f"You have {new_life} attempts remaining to guess the number ")
        elif ans == 1:
            print("Too low!")
            h_life += -1
            print(f"You have {new_life} attempts remaining to guess the number ")
    else:
        print("Invalid choice!")
        start_game = False



            

            