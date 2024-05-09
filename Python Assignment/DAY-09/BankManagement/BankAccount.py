from AccountHolder import AccountHolder
from TransactionError import TransactionError


class BankAccount(AccountHolder):
    def __init__(self, name, account_number, balance=0):
        super().__init__(name)
        self.__account_number = account_number
        self.__balance = balance
        self.__transaction_history = []

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise TransactionError("Invalid deposit amount")
        self.__balance += amount
        self.__transaction_history.append(("Deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise TransactionError("Invalid withdrawal amount")
        if amount > self.__balance:
            raise TransactionError("Insufficient balance for withdrawal")
        self.__balance -= amount
        self.__transaction_history.append(("Withdrawal", amount))

    def display_info(self):
        print("Account Holder Name:", self.get_name())
        print("Account Number:", self.get_account_number())
        print("Balance:", self.get_balance())
        print("Transaction History:")
        for transaction in self.__transaction_history:
            print(transaction)
