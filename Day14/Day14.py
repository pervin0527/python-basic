import os
from random import choice
from configs import day14_logo1, day14_logo2, day14_game_data


def get_account():
   account1 = choice(day14_game_data)
   account2 = choice(day14_game_data)


   if account1 == account2:
       account2 = choice(day14_game_data)


   return account1, account2
  


def get_answer(follower_a, follower_b):
   if follower_a > follower_b:
       return 'a'
   else:
       return 'b'


def compare(user_choice, answer):
   if user_choice == answer:
       return True
   else:
       return False


def higher_lower_game():   
   score = 0
   stop_game = False
   is_correct = True
   while not stop_game:
       os.system("clear")
       print(day14_logo1)
      
       if is_correct:
           if score > 0:
               print(f"You're right! Current score: {score}")


           A, B = get_account()
           print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
           print(day14_logo2)
           print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
          
           user_choice = input("Who has more follwers? Type 'A' or 'B': ").lower()
           answer = get_answer(A["follower_count"], B["follower_count"])
           is_correct = compare(user_choice, answer)


           if is_correct:
               score += 1
                      
       else:
           print(f"Sorry, that's wrong. Final score: {score}")
           stop_game = True


higher_lower_game()