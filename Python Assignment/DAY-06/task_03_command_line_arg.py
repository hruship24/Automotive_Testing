'''
date : 24th April 2024
Desc : Task 3:  You are given a list of numbers. Write a Python program called number_sort.py
that takes these numbers as command-line arguments and sorts them in ascending order.
If the user provides invalid input (e.g., non-numeric values), the program should handle
the exception and display an appropriate error message. If the input is valid,
the program should print the sorted list of numbers. Write the Python program to fulfill
these requirements.
'''

import sys

try:
    numbers = [int(num) for num in sys.argv[1:]]
    sorted_numbers = sorted(numbers)
    print("Sorted numbers:", sorted_numbers)

except ValueError:
    print("Error: Invalid input. Please provide numeric values only.")

except Exception as e:
    print("An error occurred:", e)