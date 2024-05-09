class ABC:
    balance=2000
    def withdraw(self):
        self.balance-=1000
        print(self.balance)
    def deposit(self):
        self.balance+=500
        print(self.balance)

a=ABC()
a.withdraw()
a.deposit()
a.withdraw()
print(a.balance)

