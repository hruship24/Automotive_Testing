import csv
import os


# Function to a csv file
def write_csv(filename):
    data = [
        ('John Doe', 30),
        ('Jane Smith',  25)
    ]

    # fieldnames = ['name', 'age']

    with open(filename, "w", newline="\n") as file:
        fileptr = csv.writer(file) #, fieldnames=fieldnames
        # fileptr.writeheader()
        fileptr.writerows(data)


def read_csv(filename):
    with open(filename, 'r', newline="\n") as file:
        reader = csv.reader(file)
        for row in reader:
            print(f"Name : {row[0]}, Age: {row[1]}")


def delete_csv(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"{filename} deleted successfully")
    else:
        print(f"{filename} does not exist")


# Main function
if __name__ == "__main__":
    filename = "data.csv"

    # Create and write data to CSV file
    write_csv(filename)

    # Read CSV file
    print("Data read from CSV file : ")
    read_csv(filename)

    # Delete CSV file
    # delete_csv(filename)