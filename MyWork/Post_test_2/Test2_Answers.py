from dataclasses import dataclass

@dataclass
class Bank:
    accounts: dict = {}
    acc_num: dict = {}
    trans_hist: list = []

    def create_account(self, cust_name, initial_balance):
        self.accounts[cust_name] = initial_balance


@dataclass
class SavingsAccount:
    interest_rate: float = 0.0

