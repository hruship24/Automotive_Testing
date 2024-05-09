'''
Date : 22nd april 2024
Desc : Program to find duplicates from a list of integers
'''

list1=[1,3,5,6,8,9,4,2,6,4,7,2,5]
list1.sort()
duplicate=[]

for i in range(len(list1)-1):
    if list1[i] == list1[i+1] :
        if list1[i] not in duplicate:
            duplicate.append(list1[i])

print('Duplicate elements form list are : ', duplicate)
