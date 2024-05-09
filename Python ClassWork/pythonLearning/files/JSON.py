import json
import os


def write_json(filename):
    data = {
        "people": [
            {"name": "John Doe", 'age': 25},
            {"name": "Hrushi Pawar", 'age': 24}
        ]
    }
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def read_json(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        for person in data["people"]:
            print(f"Name : {person['name']}, Age : {person['age']}")


def delete_json(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} does not exist")


# Main function
if __name__ == "__main__":
    filename = "data.json"

    # Create and write data to CSV file
    write_json(filename)

    # Read CSV file
    print("Data read from CSV file : ")
    read_json(filename)

    # Delete CSV file
    # delete_json(filename)
