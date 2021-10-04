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
    "water": 500,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water {resources['water']}ml")
    print(f"Milk {resources['milk']}ml")
    print(f"Coffee {resources['coffee']}g")
    print(f"Profit: ${profit}")


def deduct(choice2):
    resources["coffee"] -= MENU[choice2]["ingredients"]["coffee"]
    resources["water"] -= MENU[choice2]["ingredients"]["water"]
    resources["milk"] -= MENU[choice2]["ingredients"]["milk"]


def checkforingredients(type):
    if type == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
            if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                    checkForAmount(type)
                else:
                    print("Sorry, there is not enough coffee powder.")
            else:
                print("Sorry, there is not enough milk.")
        else:
            print("Sorry, there is not enough water.")

    if type == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
            if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
                if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                    checkForAmount(type)
                else:
                    print("Sorry, there is not enough coffee powder.")
            else:
                print("Sorry, there is not enough milk.")
        else:
            print("Sorry, there is not enough water.")

    if type == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                checkForAmount(type)
            else:
                print("Sorry, there is not enough coffee powder.")
        else:
            print("Sorry, there is not enough water.")


def checkForAmount(choice1):
    global profit
    if choice1 == "cappuccino":
        print("Please insert some coins.")
        quarter = float(input("How many quarters? "))
        dime = float(input("How many dimes? "))
        nickel = float(input("How many nickels? "))
        penny = float(input("How many pennies? "))
        customer_total = penny * 0.01 + nickel * 0.05 + quarter * 0.25 + dime * 0.10
        cost = MENU[choice1]["cost"]
        if customer_total >= cost:
            change = round(customer_total - cost, 2)
            print(f"Your change is ${change}")
            profit += cost
            deduct(choice1)
            print("Here's your Cappuccino ☕. Enjoy!")
        else:
            print("Please insert more money.")
    elif choice1 == "espresso":
        print("Please insert some coins.")
        quarter = float(input("How many quarters? "))
        dime = float(input("How many dimes? "))
        nickel = float(input("How many nickels? "))
        penny = float(input("How many pennies? "))
        customer_total = penny * 0.01 + nickel * 0.05 + quarter * 0.25 + dime * 0.10
        cost = MENU[choice1]["cost"]
        if customer_total >= cost:
            change = round(customer_total - cost, 2)
            print(f"Your change is ${change}")
            resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
            profit += cost
            print("Here's your Espresso ☕. Enjoy!")
        else:
            print("Please insert more money.")

    elif choice1 == "latte":
        print("Please insert some coins.")
        quarter = float(input("How many quarters? "))
        dime = float(input("How many dimes? "))
        nickel = float(input("How many nickels? "))
        penny = float(input("How many pennies? "))
        customer_total = penny * 0.01 + nickel * 0.05 + quarter * 0.25 + dime * 0.10
        cost = MENU[choice1]["cost"]
        if customer_total >= cost:
            change = round(customer_total - cost, 2)
            print(f"Your change is ${change}")
            profit += cost
            deduct(choice1)
            print("Here's your Latte ☕. Enjoy!")
        else:
            print("Please insert more money.")


profit = 0
end_of_game = True
while end_of_game:
    choice = input("What would you like? (espresso/latte/cappuccino) ").lower()
    if choice == "report":
        report()
    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
        checkforingredients(choice)
    elif choice == "quit":
        end_of_game = False

