'''
Date : 24th April 2024
Desc : Task-02 :Write a Python program that prompts the user to enter an index and
retrieves the element from a list at that index. The program should handle exceptions
such as IndexError and ValueError. If no exception occurs, it should print
the retrieved element. Additionally, include an else block to print the element
if no exception occurs and a finally block to ensure that the program execution is completed.
Write the Python program to fulfill these requirements.
'''

try:
    my_list = [10, 20, 30, 40, 50]
    index = int(input("Enter an index: "))
    element = my_list[index]

except ValueError:
    print("Error: Invalid input. Please enter a valid integer index.")

except IndexError:
    print("Error: Index out of range. Please enter a valid index within the range of the list.")

else:
    print("Retrieved element:", element)

finally:
    print("Program execution completed.")