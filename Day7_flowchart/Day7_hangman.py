import random
from configs import logo, stages, word_list

print(logo)
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')

display = ["_"] * len(chosen_word)
print(display)

lives = 6
while "_" in display and lives:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    else:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
    print(" ".join(display))

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            print("You lose")

    if "_" not in display:
        print("You win")

    print(stages[lives])
