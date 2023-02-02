import random

import random
from secrets import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    choose = random.choice(cards)
    return choose

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1) 
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == 0:
        return ("You won!")
    elif user_score == 0:
        return ("You Lose!")
    elif computer_score > 21:
        return ("You went above 21, You LOSE!")
    elif user_score > 21:
        return ("Computer went above 21, You WON!")
    elif user_score > computer_score:
        return ("You WON!")
    else: 
        return ("You LOSE!")


def play():
    user_cards = []
    computer_cards = []

    for i in range(0,2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} , your score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")
        is_game_over = False

        if user_cards == 0 or computer_cards == 0 or user_cards > 21:
            is_game_over = True
        else:
            y_n = input("type 'y' to add card or 'n' to end ").lower()
            if y_n == "y":
                user_score.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, Your final score: {user_score}")
    print(f"Computer final hand: {computer_cards}, Computer final score: {computer_score}")
    print(computer_score(user_score,computer_score))
  
while input("Do you want to play a game of BlackJack type 'y' else 'no': ") == "y":
    play()



