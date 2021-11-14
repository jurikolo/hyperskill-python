# Write your code here
# Initialize variables
remaining_water = 400
remaining_milk = 540
remaining_coffee = 120
remaining_cups = 9
remaining_money = 550

def print_state(water, milk, coffee, cups, money):
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")

def check_ingredients(coffee_type):
    if remaining_cups < 1:
        return False
    if coffee_type == "1":
        if (remaining_water < 250
                or remaining_coffee < 16):
            return False
    if coffee_type == "2":
        if (remaining_water < 350
                or remaining_milk < 75
                or remaining_coffee < 20):
            return False
    if coffee_type == "3":
        if (remaining_water < 200
                or remaining_milk < 100
                or remaining_coffee < 12):
            return False
    return True

while True:
    print("Write action (buy, fill, take):")
    action = input()
    if action == "exit":
        break
    elif action == "remaining":
        print_state(remaining_water, remaining_milk, remaining_coffee, remaining_cups, remaining_money)
    elif action == "fill":
        print("Write how many ml of water you want to add:")
        remaining_water += int(input())
        print("Write how many ml of milk you want to add:")
        remaining_milk += int(input())
        print("Write how many grams of coffee beans you want to add:")
        remaining_coffee += int(input())
        print("Write how many disposable coffee cups you want to add:")
        remaining_cups += int(input())
    elif action == "take":
        print("I gave you $", remaining_money)
        remaining_money = 0
    elif action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        coffee_type = input()
        has_ingredients = check_ingredients(coffee_type)
        if has_ingredients:
            if coffee_type == "1":
                remaining_water -= 250
                remaining_coffee -= 16
                remaining_money += 4
                remaining_cups -= 1
            elif coffee_type == "2":
                remaining_water -= 350
                remaining_milk -= 75
                remaining_coffee -= 20
                remaining_money += 7
                remaining_cups -= 1
            elif coffee_type == "3":
                remaining_water -= 200
                remaining_milk -= 100
                remaining_coffee -= 12
                remaining_money += 6
                remaining_cups -= 1