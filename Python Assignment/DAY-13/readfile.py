import os


def read_text(filename):
    try:
        with open(filename, 'r', newline="\n") as file:
            for line in file:
                print(line)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        

if __name__ == "__main__":
    filename = "C:\\Users\\Administrator\\Desktop\\Python Atomotive testing\\Assignment\\DAY-13\\data.txt"

    # Read text file
    print("Data read from CSV file : ")
    read_text(filename)