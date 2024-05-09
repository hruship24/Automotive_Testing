'''
Date : 22nd April 2024
Desc : Write a Python script to create, update, and print
a dictionary containing personal information (like name, age, city).
'''


def create_person():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")
    return {'name': name, 'age': age, 'city': city}

def update_person_info(person_dict):
    print("Current information:", person_dict)
    choice = input("What information do you want to update (name/age/city)? Enter 'none' to skip: ")
    match choice.lower():
        case 'name':
            person_dict['name'] = input("Enter new name: ")
        case 'age':
            person_dict['age'] = int(input("Enter new age: "))
        case 'city':
            person_dict['city'] = input("Enter new city: ")
        case 'none':
            pass
        case _:
            print("Invalid choice.")

def print_person_info(person_dict):
    print("\nPersonal Information:")
    print("Name:", person_dict['name'])
    print("Age:", person_dict['age'])
    print("City:", person_dict['city'])

# Call create_person directly to start the script
person_info = create_person()
print_person_info(person_info)

update = input("Do you want to update any information (yes/no)? ")
if update.lower() == 'yes':
    update_person_info(person_info)
    print_person_info(person_info)