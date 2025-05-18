# Encapsulatio : hide details
# acces Modifier - public ,protected, privet


class Bank:
    def __init__(self, holder_name, initial_deposite):
        self.holder_name = holder_name  # public
        self._branch = "banani 11"  # Protected
        self.__balance = initial_deposite  # privet

    def deposite(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f"fokira taka ny "


rafsan = Bank("chuto bro", 10000)


print(rafsan.holder_name)
rafsan.holder_name = "boro vai"
# print(rafsan.__balance)
rafsan.deposite(5020000)
print(rafsan.get_balance())
# rafsan.balance = 0
# print(rafsan)
print(rafsan.holder_name)
print(rafsan._branch)

print(dir(rafsan))
