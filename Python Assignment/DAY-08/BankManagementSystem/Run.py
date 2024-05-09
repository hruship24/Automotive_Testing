from BankAccount import BankAccount
from SavingAccount import SavingAccount

# bankAcc = BankAccount('Hrushikesh', 1234, 54321)
savingAcc = SavingAccount('Hrushi', 5678, 10000, 10)

# w1 = bankAcc.withdraw(100)
# print('After withdrawal, balance is ', w1)
# d1 = bankAcc.deposit(100)
# print('After deposit, balance is ', d1)
w2 = savingAcc.withdraw(200)
print('After withdrawal, balance is ', w2)
d2 = savingAcc.deposit(200)
print('After deposit, balance is ', d2)
interest = savingAcc.calculateInterest()
print('After interest, Total balance is ',interest)

