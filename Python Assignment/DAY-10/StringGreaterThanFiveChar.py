'''
Desc : Task 7: Write a Python program that takes a list of strings as input and returns a new list containing
only the strings that have 5 or more characters in it
'''

input_list = ["hello", "world", "python", "programming", "is", "awesome"]

result_list = [string for string in input_list if len(string) >= 5]

print(result_list)