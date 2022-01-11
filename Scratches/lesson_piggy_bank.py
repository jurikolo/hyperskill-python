class PiggyBank:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        self.dollars += deposit_dollars
        self.cents += deposit_cents
        if self.cents > 99:
            self.dollars += self.cents // 100
            self.cents %= 100

my_piggy_bank = PiggyBank(1, 1)
my_piggy_bank.add_money(2, 0)
print(my_piggy_bank.dollars)
print(my_piggy_bank.cents)

my_piggy_bank_2 = PiggyBank(1, 1)
my_piggy_bank2.add_money(102)
print(my_piggy_bank.dollars)
print(my_piggy_bank.cents)