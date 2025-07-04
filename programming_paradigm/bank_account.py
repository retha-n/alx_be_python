class BankAccount:
    def __init__(self, account_balance, initial_balance):
        self.account_balance = account_balance
        self.initial_balance = 0

    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount): 
        if self.account_balance <= self.initial_balance:
            return False
        else:
            self.account_balance -= amount
            return True
    def display_balance(self):
        print(f"The Bank account's current Balance is {self.account_balance}")



    