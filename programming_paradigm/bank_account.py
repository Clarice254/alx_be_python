# bank_account.py
class BankAccount:
    def __init__(self, account_balance = 0):
        """Initialize the account balance."""
        self.account_balance = account_balance

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """Deduct the amount from the account balance if funds are sufficient."""
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")