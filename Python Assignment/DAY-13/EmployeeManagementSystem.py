import json
import os


EMPLOYEE_FILE = "C:\\Users\\Administrator\\Desktop\\Python Atomotive testing\\Assignment\\DAY-13\\employees.json"


def load_employees():
    try:
        with open(EMPLOYEE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_employees(employees):
    with open(EMPLOYEE_FILE, "w") as file:
        json.dump(employees, file, indent=4)


def add_employee(employee):
    employees = load_employees()
    employees[employee["id"]] = employee
    save_employees(employees)
    print("Employee added successfully.")


def update_employee(employee_id, new_data):
    employees = load_employees()
    if employee_id in employees:
        employees[employee_id].update(new_data)
        save_employees(employees)
        print("Employee updated successfully.")
    else:
        print("Employee not found.")


def delete_employee(employee_id):
    employees = load_employees()
    if employee_id in employees:
        del employees[employee_id]
        save_employees(employees)
        print("Employee deleted successfully.")
    else:
        print("Employee not found.")


def get_employee(employee_id):
    employees = load_employees()
    if employee_id in employees:
        print("Employee Details:")
        print(json.dumps(employees[employee_id], indent=4))
    else:
        print("Employee not found.")


def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Delete Employee")
        print("4. Get Employee Details")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            employee = {}
            employee["id"] = input("Enter employee ID: ")
            employee["name"] = input("Enter employee name: ")
            employee["position"] = input("Enter employee position: ")
            add_employee(employee)
        elif choice == "2":
            employee_id = input("Enter employee ID to update: ")
            new_data = {}
            new_data["name"] = input("Enter new name: ")
            new_data["position"] = input("Enter new position: ")
            update_employee(employee_id, new_data)
        elif choice == "3":
            employee_id = input("Enter employee ID to delete: ")
            delete_employee(employee_id)
        elif choice == "4":
            employee_id = input("Enter employee ID to get details: ")
            get_employee(employee_id)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()