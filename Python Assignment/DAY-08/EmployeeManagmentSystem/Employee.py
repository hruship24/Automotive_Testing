from Person import Person


class Employee(Person):

    def __init__(self, name, employee_id, salary):
        super().__init__(name)
        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display_info(self):
        print("Employee Name:", self.get_name())
        print("Employee ID:", self.get_employee_id())
        print("Salary:", self.__salary)