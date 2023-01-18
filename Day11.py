import os
from random import choice
from configs import blackjack_logo

def print_states(player, dealer, is_final=False):
    if not is_final:
        print(f"    Your cards: {player}, current score: {sum(player)}")
        print(f"    Computer's first card: {dealer[0]}")
    else:
        print(f"    Your final hand: {player}, final score: {sum(player)}")
        print(f"    Computre's final hand: {dealer}, final score: {sum(dealer)}")

def init_get_cards():
    player_cards, dealer_cards = [choice(deck) for _ in range(2)], [choice(deck) for _ in range(2)]
    print_states(player_cards, dealer_cards)

    return player_cards, dealer_cards

def check_is_blackjack(player, dealer):
    if sum(player) == 21:
        print_states(player, dealer, True)
        print("Win with a Blackjack.")
    elif sum(dealer) == 21:
        print_states(player, dealer, True)
        print("Lose, opponent has Blackjack.")
        

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_game = input("Type 'y' to get another card, type 'n' to pass:")
while play_game == "y":
    os.system("clear")
    print(blackjack_logo)

    ## 처음 카드를 받는다.
    player_cards, dealer_cards = init_get_cards()
    ## blackjack 여부 검사
    check_is_blackjack(player_cards, dealer_cards)

    get_card = 'y'
    while get_card == 'y':
        ## 새로운 카드를 받을 것인가?
        get_card = input("Type 'y' to get another card, type 'n' to pass: ")
        
        ## 받는다.
        if get_card == 'y':
            player_cards.append(choice(deck))
            print_states(player_cards, dealer_cards)
            
            ## bust 여부 검사
            if sum(player_cards) > 21:
                print_states(player_cards, dealer_cards, True)
                print("You went over. You lose.")
                get_card = 'n'

        ## 받지 않는다.
        else:
            ## 딜러의 카드 합이 17미만인 경우 추가 카드 받기.
            while sum(dealer_cards) < 17:
                dealer_cards.append(choice(deck))

            print_states(player_cards, dealer_cards, True)
            if sum(dealer_cards) > 21:
                print("Opponent went over. You win.")
            elif sum(player_cards) == sum(dealer_cards):
                print("Draw.")
            elif sum(player_cards) > sum(dealer_cards):
                print("You win.")
            else:
                print("You lose.")
            get_card = 'n'
                
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")