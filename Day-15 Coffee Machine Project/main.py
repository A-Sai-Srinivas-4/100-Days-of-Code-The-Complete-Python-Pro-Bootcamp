from numbers import Number

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 60.00,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 70.00,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 80.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
is_on = True

def process_coins():
    total = int(input("Please Enter Your Amount(Rs):"))
    return total


def check_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def is_transaction_successful(money_received,drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is your {change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Your money refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ Enjoy..!")


while is_on:
    coffee_choice = input(
        "Menu:\n"
        "espresso - Rs60\n"
        "latte - Rs70\n"
        "cappuccino - Rs80\n"
        "What would you like?\n"
    ).lower()
    if coffee_choice == "off":
        is_on = False
        print("Thank you Come Again")
    elif coffee_choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[coffee_choice]
        if check_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(coffee_choice,drink["ingredients"])

