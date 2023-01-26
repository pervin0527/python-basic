from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_on = True
# my_coffee_items = MenuItem()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()
my_pay_machine = MoneyMachine()

is_machine_on = True
while is_machine_on:
	choice = input(f"What would you like? {my_menu.get_items()}: ")

	if choice == "off":
		is_machine_on = False

	elif choice == "report":
		my_coffee_maker.report()
		my_pay_machine.report()

	elif my_menu.find_drink(choice):
		my_coffee = my_menu.find_drink(choice)
		if my_coffee_maker.is_resource_sufficient(my_coffee):
			if my_pay_machine.make_payment(my_coffee.cost):
				my_coffee_maker.make_coffee(my_coffee)

		# if my_coffee_maker.is_resource_sufficient(my_coffee) and my_pay_machine.make_payment(my_coffee.cost):
		# 		my_coffee_maker.make_coffee(my_coffee)