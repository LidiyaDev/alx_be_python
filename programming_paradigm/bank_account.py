# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")

if __name__ == "__main__":
    # For testing purposes only
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(30)
    account.display_balance()
