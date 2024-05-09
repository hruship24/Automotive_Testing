from Employee import Employee


class Manager(Employee):

    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.__department = department

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def display_info(self):
        super().display_info()
        print("Department:", self.get_department())
