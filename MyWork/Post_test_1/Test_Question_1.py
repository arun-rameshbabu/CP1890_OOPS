
"""
I wasn't able to finish this question
unfinished  code was commented out so it wouldn't error when run.
"""

class Bank:
    def __init__(self):
        self.accounts = dict()
        self.account_number = 0
        self.transaction_history = []

    def create_account(self, customer_name, initial_balance):
        self.accounts[customer_name] = initial_balance

    def deposit(self, customer_name=str, amount=float):
        account = self.accounts.pop(customer_name)
        self.accounts[customer_name] = account + amount

"""
class SavingsAccount(Bank):
    def __init__(self):
        interest_rate: float = 0.0
"""

bank = Bank()
bank.create_account('Alice', 1000)
# savings_account = SavingsAccount()
#savings_account.interest_rate = 0.05
#savings_account.create_account('Bob', 2000)
#savings_account.deposit('Bob', 1000)
#savings_account.calculate_interest('Bob')
