import random

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    global chance
    if difficulty == "easy":
        chance = EASY_LEVEL_CHANCE
    else:
        chance = HARD_LEVEL_CHANCE

def check_answer(number, answer, remain):
    if number == answer:
        print(f"You got it! The answer was {answer}.")
        return 

    elif number > answer:
        print("Too high.")
        return remain - 1

    else:
        print("Too low.")
        return remain - 1


EASY_LEVEL_CHANCE = 10
HARD_LEVEL_CHANCE = 5
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1, 100)

chance = 0
set_difficulty()
print(f"You have {chance} attemps remaining to guess the number.")

while chance > 0:
    input_number = int(input(f"remain #{chance}. Make a guess: "))
    chance = check_answer(input_number, answer, chance)

    if chance == 0:
        print(f"You've run out of guesses. You lose. The answer is {answer}.")

    if chance == None:
        chance = -1