from AccountHolder import AccountHolder


class BankAccount(AccountHolder):
    def __init__(self, accHoldName, accNum, balance):
        super().__init__(accHoldName)
        self.__accNum = accNum
        self.__balance = balance

    def get_accNum(self):
        return self.__accNum

    def set_accNum(self, accno):
        self.__accNum = accno

    def get_balance(self):
        return  self.__balance

    def set_balance(self,bal):
        self.__balance = bal

    def deposit(self,amount):
        print('Balance before deposit is ',self.__balance)
        self.__balance += amount
        return self.__balance

    def withdraw(self,amount):
        print('Balance before withdrawal is ', self.__balance)
        self.__balance -= amount
        return self.__balance


