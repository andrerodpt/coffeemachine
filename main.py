from data import MENU, resources


def print_resource(resource, unit):
    print(f"{resource.capitalize()}: {resources[resource]}{unit}")


def print_report():
    for resource in resources:
        if resource == 'water' or resource == 'milk':
            print_resource(resource, 'ml')
        elif resource == 'coffee':
            print_resource(resource, 'g')
        else:
            print(f"{resource.capitalize()}: ${resources['money']}")
    if 'money' not in resources:
        print("Money: $0")


def check_resources_available(choice):
    for ingredient in MENU[choice]['ingredients']:
        if MENU[choice]['ingredients'][ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    quarters = int(input("Quarters: "))
    dimes= int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    return quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01


def add_money_to_machine(beverage_cost):
    if 'money' not in resources:
        resources['money'] = beverage_cost
    else:
        resources['money'] += beverage_cost


def check_transaction(total_amount, choice):
    beverage_cost = MENU[choice]['cost']
    if total_amount < beverage_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(total_amount - beverage_cost, 2)
        add_money_to_machine(beverage_cost)
        print(f"Here is ${change} dollars in change.")
        return True


def make_coffee(choice):
    for ingredient in MENU[choice]['ingredients']:
        resources[ingredient] -= MENU[choice]['ingredients'][ingredient]
    print(f"Here is your {choice}. Enjoy!")


def process_choice(choice):
    has_resources = check_resources_available(choice)
    if has_resources:
        transaction_ok = check_transaction(process_coins(), choice)
        if transaction_ok:
            make_coffee(choice)


coffee_machine_on = True
while coffee_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        coffee_machine_on = False
    elif choice == 'report':
        print_report()
    elif choice in MENU:
        process_choice(choice)
