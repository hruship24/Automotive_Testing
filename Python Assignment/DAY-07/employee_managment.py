'''
Date : 25th April 2024
Desc :  Employee Management System
You are developing an employee management system for a company. Implement a class called
Employee with the following specifications:
The class should have private instance variables for employee ID, name, and salary.
Include a constructor to initialize these variables.
Implement getter and setter methods for each instance variable.
Implement a method to display employee information.
Implement a method to give a salary hike to an employee. The method should accept
a percentage value by which the salary will be increased.
Write a Python program to demonstrate the functionality of the Employee class
by creating instances, displaying employee information, giving salary hikes, and
displaying updated employee information.
'''

class Employee:
    def _init_(self, emp_id, name, salary):
        self.__emp_id = emp_id
        self.__name = name
        self.__salary = salary

    def get_emp_id(self):
        return self.__emp_id

    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):
        print("Employee ID:", self.__emp_id)
        print("Name:", self.__name)
        print("Salary:", self.__salary)

    def give_salary_hike(self, percentage):
        self._salary += (self._salary * percentage) / 100


emp1 = Employee(101, "John Doe", 50000)
emp1.display_info()
print()

emp1.give_salary_hike(10)
print("Employee after salary hike:")
emp1.display_info()