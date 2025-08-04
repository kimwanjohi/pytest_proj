class BankAccount:
    def __init__(self, initial_balance=0, overdraft_limit=0):
        self.balance = initial_balance
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance - amount < -self.overdraft_limit:
            raise ValueError("Insufficient funds: overdraft limit exceeded.")
        self.balance -= amount

    def get_balance(self):
        return self.balance
