from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine = MoneyMachine()
menu = Menu()
coffeemaker = CoffeeMaker()

is_on = True
while is_on:
    choice = input(f"What would you like? ({menu.get_items()}) ")
    if choice == "report":
        moneymachine.report()
        coffeemaker.report()
    elif choice == "off":
        is_on = False
    else:
        object = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(object):
            if moneymachine.make_payment(object.cost):
                coffeemaker.make_coffee(object)

       



