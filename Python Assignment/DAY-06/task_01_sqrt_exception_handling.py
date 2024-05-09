'''
Date : 24th April 2024
Desc : Task 1:You are tasked with creating a Python program that
calculates the square root of a non-negative number entered by the user.
The program should handle exceptions such as ValueError and NameError appropriately.
Additionally, it should include an else block to print the square root if no exception occurs
and a finally block to ensure that the program execution is completed.
Write the Python program to fulfill these requirements.
'''
from  math import sqrt

try:
    num = int(input("Enter a non-negative number: "))
    if num < 0:
        raise ValueError("The number must be non-negative.")

    square_root = sqrt(num)

except ValueError as ve:
    print("Error:", ve)

except NameError:
    print("Error: Invalid input. Please enter a valid number.")

else:
    print("Square root:", square_root)

finally:
    print("Program execution completed.")
