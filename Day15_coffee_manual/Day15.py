def print_resources(current_resource, money):
    for key in current_resource:
        print(f"{key.title()} :  {current_resource[key]}")
    print(f"Money : ${money}")

def check_sufficient(ingredients, resources):
    for key in ingredients:
        target = ingredients[key]
        remain = resources[key]

        if remain < target:
            print(f"Sorry there is not enough {key}.")
            return False
        else:
            return True

def pay(cost):
    print("Please insert coins.")
    quarters = float(input("How many quarters?: ")) * 0.25 ## 0.25
    dimes = float(input("How many dimes?: ")) * 0.10 ## 0.10
    nickles = float(input("How many nickles?: ")) * 0.05 ## 0.05
    pennis = float(input("How many pennis?: ")) * 0.01 ## 0.01

    total_pay = (quarters + dimes + nickles + pennis)
    if total_pay < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    else:
        remainder = total_pay - cost
        print(f"Here is ${remainder:.2f} in change.")
        return True

def make_coffee(ingredients, resources):
    for key in ingredients:
        resources[key] -= ingredients[key]

    return resources


def coffe_machince():
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        }
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    profit = 0
    turn_on = True
    while turn_on:
        user_choice = input("What would you like? (espresso/latte/cappuccino: ")

        if user_choice == "off":
            print("Good Bye.")
            turn_on = False

        elif user_choice == "report":
            print_resources(resources, profit)

        elif user_choice in MENU:
            coffee = MENU[user_choice]
            if check_sufficient(coffee["ingredients"], resources):
                is_can_pay = pay(coffee["cost"])

                if is_can_pay:
                    resources = make_coffee(coffee["ingredients"], resources)
                    profit += coffee["cost"]
                    print(f"Here is your {user_choice}. Enjoy!")

coffe_machince()