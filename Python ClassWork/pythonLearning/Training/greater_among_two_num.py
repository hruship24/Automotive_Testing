'''
Date : 18th April 2024
Desc : Biggest of two numbers
'''

first_number  = int(input('Enter first number :'))
second_number = int(input('Enter second number :'))

if first_number == second_number :
    print('Both numbers are equal')
elif first_number > second_number :
    print(first_number,' is the greatest')
else :
    print(second_number,' is the greatest')
