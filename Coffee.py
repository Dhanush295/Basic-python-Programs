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


def is_resource(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            return False
    return True


def process_coins():
    print("Please insert coin: ")
    quarter = int(input("How many Quarters: "))
    dime = int(input("How many Dime: "))
    nickel = int(input("How many Nickel: "))
    pennies = int(input("How many Pennies: "))

    total = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (pennies * 0.01)
    return total


def is_successfull(payment, drink_cost):
    if payment > drink_cost:
        change = payment - drink_cost
        print(f"Your change is: {change}")
        return True
    else:
        print("Sorry money is insufficient!")
        return False


def make_coffee(drink_name, order_ing):
    for item in order_ing:
        resources[item] -= order_ing[item]
        print(f"Here is your drink: {drink_name}")




loop = True

while loop:
    user_coffee = input("What would you like (espresso/latte/cappuccino):")
    if user_coffee == "of":
        loop = False
    elif user_coffee == "report":
        print(f"water is {resources['water']} ml")
        print(f"milk is {resources['milk']} ml")
        print(f"coffee is {resources['coffee']} ml")
    else:
        drink = MENU[user_coffee]
        if is_resource(drink["ingredients"]):
            payment = process_coins()
            if is_successfull(payment,drink["cost"]):
                make_coffee(user_coffee,drink["ingredients"])



