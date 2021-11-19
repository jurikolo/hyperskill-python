class CoffeeMachine:
    def __init__(self):
        self.remaining_water = 400
        self.remaining_milk = 540
        self.remaining_coffee = 120
        self.remaining_cups = 9
        self.remaining_money = 550
        self.state = "choosing an action"

    def get_state(self):
        return self.state

    def get_remainings(self):
        return self.remaining_water, \
               self.remaining_milk, \
               self.remaining_coffee, \
               self.remaining_cups, \
               self.remaining_money

    def add_water(self, amount):
        self.remaining_water += amount

    def add_milk(self, amount):
        self.remaining_milk += amount

    def add_coffee(self, amount):
        self.remaining_coffee += amount

    def add_cups(self, amount):
        self.remaining_cups += amount

    def money_withdrawal(self):
        amount = self.remaining_money
        self.remaining_money = 0
        return amount

    def set_state(self, state):
        self.state = state

    def check_cups(self):
        if self.remaining_cups < 1:
            return False
        return True

    def check_water(self, coffee_type):
        if coffee_type == "1":
            if self.remaining_water < 250:
                return False
            return True
        if coffee_type == "2":
            if self.remaining_water < 350:
                return False
            return True
        if coffee_type == "3":
            if self.remaining_water < 200:
                return False
            return True

    def check_milk(self, coffee_type):
        if coffee_type == "1":
            return True
        if coffee_type == "2":
            if self.remaining_milk < 75:
                return False
            return True
        if coffee_type == "3":
            if self.remaining_milk < 100:
                return False
            return True

    def check_coffee(self, coffee_type):
        if coffee_type == "1":
            if self.remaining_coffee < 16:
                return False
            return True
        if coffee_type == "2":
            if self.remaining_coffee < 20:
                return False
            return True
        if coffee_type == "3":
            if self.remaining_coffee < 12:
                return False
            return True

    def prepare_a_coffee(self, coffee_type):
        self.remaining_cups -= 1
        if coffee_type == "1":
            self.remaining_water -= 250
            self.remaining_coffee -= 16
            self.remaining_money += 4
        elif coffee_type == "2":
            self.remaining_water -= 350
            self.remaining_milk -= 75
            self.remaining_coffee -= 20
            self.remaining_money += 7
        elif coffee_type == "3":
            self.remaining_water -= 200
            self.remaining_milk -= 100
            self.remaining_coffee -= 12
            self.remaining_money += 6

coffee_machine = CoffeeMachine()

while True:
    if coffee_machine.get_state() == "choosing an action":
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "exit":
            break
        elif action == "remaining":
            remainings = coffee_machine.get_remainings()
            print("The coffee machine has:")
            print("{} of water\n"
                  "{} of milk\n"
                  "{} of coffee beans\n"
                  "{} of disposable cups\n"
                  "${} of money".format(remainings[0], remainings[1], remainings[2], remainings[3], remainings[4]))
        elif action == "fill":
            print("Write how many ml of water you want to add:")
            coffee_machine.add_water(int(input()))
            print("Write how many ml of milk you want to add:")
            coffee_machine.add_milk(int(input()))
            print("Write how many grams of coffee beans you want to add:")
            coffee_machine.add_coffee(int(input()))
            print("Write how many disposable coffee cups you want to add:")
            coffee_machine.add_cups(int(input()))
        elif action == "take":
            print("I gave you ${}".format(coffee_machine.money_withdrawal()))
        elif action == "buy":
            coffee_machine.set_state("choosing a type of coffee")

    if coffee_machine.get_state() == "choosing a type of coffee":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        coffee_type = input()
        if coffee_type != "back":
            if not coffee_machine.check_water(coffee_type):
                print("Sorry, not enough water")
            elif not coffee_machine.check_milk(coffee_type):
                print("Sorry, not enough milk")
            elif not coffee_machine.check_coffee(coffee_type):
                print("Sorry, not enough coffee")
            elif not coffee_machine.check_cups():
                print("Sorry, not enough cups")
            else:
                print("I have enough resources, making you a coffee!")
                coffee_machine.prepare_a_coffee(coffee_type)
        coffee_machine.set_state("choosing an action")
