import os
from random import choice
from configs import day14_logo1, day14_logo2, day14_game_data

def get_account():
    account = choice(day14_game_data)

    return account

def print_account(A, B):
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print(day14_logo2)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}")

def compare(follower_a, follower_b, guess):
    if follower_a > follower_b:
        return guess == 'a'
    else:
        return guess == 'b'


def game():
    score = 0
    is_game_over = False
    account_b = get_account()

    print(day14_logo1)
    while not is_game_over:

        account_a = account_b
        account_b = get_account()
        while account_a == account_b:
            account_b = get_account()
        print_account(account_a, account_b)

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = compare(account_a["follower_count"], account_b["follower_count"], guess)

        os.system("clear")
        print(day14_logo1)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            is_game_over = True
            print(f"Sorry that's wron. Final score: {score}")

game()