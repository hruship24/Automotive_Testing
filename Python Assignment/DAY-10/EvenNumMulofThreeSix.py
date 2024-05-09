'''
Desc : Task 6: Write a Python program that takes a list of integers as input and returns a new list containing
only the even numbers that are multiples of 3 and 6.
'''

input_numbers = [12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72]

result_list = [num for num in input_numbers if num % 2 == 0 and num % 3 == 0 and num % 6 == 0]

print(result_list)