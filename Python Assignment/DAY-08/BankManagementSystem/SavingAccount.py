from BankAccount import BankAccount


class SavingAccount(BankAccount):
    def __init__(self, accHoldName, accNum, balance, interestRate):
        super().__init__(accHoldName, accNum, balance)
        self.__interestRate = interestRate

    def get_interestRate(self):
        return  self.__interestRate

    def set_interestRate(self, rate):
        self.__interestRate = rate

    def calculateInterest(self):
        interest = self.get_balance() * (self.__interestRate / 100)
        total = self.get_balance() + interest
        return total

