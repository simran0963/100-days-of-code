from menu import Menu,MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
import os

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
mac_on = True

def clear():
	os.system('cls')
clear()
while mac_on:
	options = menu.get_items()
	choice = input(f"What would you like? ({options}):")
	if choice =="off":
		is_on = False
	elif choice == "report":
		money_machine.report()
		coffee_maker.report()
	else:
		drink = menu.find_drink(choice)
		if coffee_maker.is_resource_sufficient(drink):
			print(money_machine.make_payment(drink.cost))