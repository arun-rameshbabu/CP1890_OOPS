from dataclasses import dataclass


@dataclass
class Bank:
    accounts: dict
    account_number: int
    transaction_history: list

    def create_account(self, customer_name: str, initial_balance: float):
        self.accounts = {customer_name: initial_balance}
        self.transaction_history.append(initial_balance)

    def deposit(self, customer_name: str, amount: float):
        self.accounts[customer_name]['balance'] += amount
        self.transaction_history.append('deposit' + str(amount))

    def withdraw(self, customer_name: str, amount: float):
        self.accounts[customer_name]['balance'] -= amount
        self.transaction_history.append('withdrew' + str(amount))

    def get_balance(self, customer_name: str):
        return self.accounts[customer_name]['balance']

    def get_transaction_history(self):
        return self.transaction_history

    def transfer(self, sender_name: str, receiver_name: str, amount: float):
        self.accounts[sender_name]['balance'] -= amount
        self.accounts[receiver_name]['balance'] += amount


bank1 = Bank({}, 1, [])
bank1.create_account('tyson harris', 1000.50)
# bank1.deposit('tyson harris', 200)
print(bank1)