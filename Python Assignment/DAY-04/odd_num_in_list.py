'''
Date : 22nd April 2024
Desc : Python program to print odd numbers in list
'''

list1=[1,2,3,4,5,6,7,8,9]
print('Odd numbers from lists are : ')
for num in list1:
    if num % 2 != 0 :
        print(num,end=' ')
