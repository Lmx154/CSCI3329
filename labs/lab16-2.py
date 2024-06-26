class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Withdrawal amount must be positive and not exceed the current balance.")

    def get_balance(self):
        return self.__balance


account = BankAccount(100)

account.deposit(200)
print(f"Balance after depositing $200: {account.get_balance()}")

account.withdraw(150)
print(f"Balance after withdrawing $150: {account.get_balance()}")

account.withdraw(400)
print(f"Balance after attempting to withdraw $400: {account.get_balance()}")
