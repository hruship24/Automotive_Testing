'''
Date : 25th April 2024
Desc : Question 2: Bank Account Management System
You are tasked with creating a simple bank account management system in Python.
Implement a class called BankAccount with the following specifications:
The class should have private instance variables for account number, account holder name,
and balance.
Include a constructor to initialize these variables.
Implement getter and setter methods for each instance variable to ensure encapsulation.
Implement methods to deposit and withdraw money from the account.
Ensure that the withdraw method checks if the account has sufficient balance before
allowing withdrawal.
Write a Python program to demonstrate the functionality of the BankAccount class by
creating instances, depositing and withdrawing money, and displaying account information.
'''

class BankAccount:

    def __init__(self):
        self.__account_number = 1234
        self.__account_holder = 'Hrushi'
        self.__balance = 87654321

    def get_account_number(self):
        return  self.__account_number
    def set_account_number(self,value):
        self.__account_number=value

    def get_account_holder(self):
        return  self.__account_holder
    def set_account_number(self,value):
        self.__account_holder=value

    def get_balance(self):
        return  self.__balance
    def set_account_number(self,value):
        self.__balance=value

    def deposit(self,value):
        self.__balance +=value
        return self.__balance

    def withdrawl(self,value):
        if value < self.__balance:
            self.__balance -=value
            return self.__balance
        else :
            return 'Insufficient Balance !!!'

    def display(self):
        print('Account No : ',self.__account_number,'\nAccount Holder Name : ',self.__account_holder,'\nBalance : ',self.__balance)

ac = BankAccount()
ac.display()
dep = ac.deposit(500)
print('Total Balance After deposit is ', dep)
withdraw = ac.withdrawl(500)
print('Total Balance After deposit is ',withdraw)

