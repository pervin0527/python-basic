import os
from configs import auction_logo

print(auction_logo)
print("Welcome to the secret auction program.")

bidder_dict = {}
bidders = True
while bidders:
    name = input("What is your name?:")
    bid = int(input("What's your bid?: $"))
    others = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    bidder_dict[name] = bid

    if others == "no":
        bidders = False
    else:
        os.system("clear")

top_name, top_bid = "", 0
for n, b in bidder_dict.items():
    if b > top_bid:
        top_name = n
        top_bid = b

print(f"The winner is {top_name} with a bid of ${top_bid}")
