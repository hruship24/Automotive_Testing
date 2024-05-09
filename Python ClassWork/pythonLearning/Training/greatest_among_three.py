'''
Date : 18th April 2024
Desc : Greatest of three number
'''

num1 = int(input('Enter the first number : '))
num2 = int(input('Enter the Second number : '))
num3 = int(input('Enter the three number : '))

if (num1 == num2 == num3):
    print('All numbers are equal')
elif (num1 > num2) and (num1>num3):
    print('Number ( ',num1,' ) is the greatest')
elif (num2 > num3):
    print('Number ( ',num2,' ) is the greatest')
else :
    print('Number ( ',num3,' ) is the greatest')



