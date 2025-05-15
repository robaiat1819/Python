class bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"fokira. you can withdraw below {self.min_withdraw}")
        elif amount > self.max_withdraw:
            print(f"bank fokir hoiye jabe you can not more than{self.max_withdraw}")
        else:
            self.balance -= amount
            print(f"here is your money {amount}")
            print(f" your balance after withdraw :  {self.balance}")


# this is brac bank

brac = bank(15000)
brac.withdraw(25)
brac.withdraw(100)
brac.withdraw(1890)
brac.withdraw(1500)

# this dbbl bank ltd
print("start bddl")
dbbl = bank(5000)
dbbl.deposit(2000)
dbbl.deposit(2000)
print(dbbl.get_balance())
