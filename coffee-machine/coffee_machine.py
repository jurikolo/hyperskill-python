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

def execute_operation(water, milk, coffee, cups, money, action):
    if not ((action == "fill") or (action == "take")):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        coffee_type = input()
        if coffee_type == "1":
            water -= 250
            coffee -= 16
            money += 4
            cups -= 1
        elif coffee_type == "2":
            water -= 350
            milk -= 75
            coffee -= 20
            money += 7
            cups -= 1
        elif coffee_type == "3":
            water -= 200
            milk -= 100
            coffee -= 12
            money += 6
            cups -= 1
    elif action == "fill":
        print("Write how many ml of water you want to add:")
        water += int(input())
        print("Write how many ml of milk you want to add:")
        milk += int(input())
        print("Write how many grams of coffee beans you want to add:")
        coffee += int(input())
        print("Write how many disposable coffee cups you want to add:")
        cups += int(input())
    elif action == "take":
        print("I gave you $", money)
        money = 0

    return water, milk, coffee, cups, money


print_state(remaining_water, remaining_milk, remaining_coffee, remaining_cups, remaining_money)
print("Write action (buy, fill, take):")
action = input()
remaining_water, remaining_milk, remaining_coffee, remaining_cups, remaining_money = execute_operation(
    remaining_water, remaining_milk, remaining_coffee, remaining_cups, remaining_money, action)
print_state(remaining_water, remaining_milk, remaining_coffee, remaining_cups, remaining_money)