'''
Date : 22nd April 2024
Desc : Python program to find N largest element from a list
'''

list1=[5,3,6,2,7,1,9,4,8]

list1.sort(reverse=True)
print('Total elements : ',len(list1))
ele= int(input('How many largest element you want : '))

if ele > 0 and ele < len(list1):
    print('The ',ele,' largest elements from list are ',list1[:ele] )
else :
    print('Entered invalid index . Program Exited ....')
