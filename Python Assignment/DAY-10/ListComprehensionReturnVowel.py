'''
Desc : Task 5: Write a Python program that takes a list of strings as input and returns a new list containing
only the strings that have three or more vowels.
'''

input_list = ["hello", "world", "python", "programming", "is", "awesome"]

result_list = [string for string in input_list if sum(1 for char in string if char.lower() in 'aeiou') >= 3]

print(result_list)