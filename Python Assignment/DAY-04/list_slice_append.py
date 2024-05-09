'''
Date : 22nd April 2024
Desc : Create a Python list and demonstrate list slicing and
       appending new elements
'''
# list[start:end:step]

list1= [1,2,3,4,5,6,7,8,9,10]

#It will print all the list elements
operation1 = list1[:]
print(operation1)

#It will print list in reverse order
operation2 = list1[::-1]
print(operation2)

#To get specific elements from list
operation3 = list1[3:8]
print(operation3)

#slice with negative indices
operation4 = list1[-7:-2]
print(operation4)

#slice with positive and negative indices
operation5 = list1[2:-5]
print(operation5)

#specific step of slicing
#It will print elements from 2 index to 7 with step of 2 
operation6 = list1[2:7:2]
print(operation6)


#Negative step size
#It will print from end to start point with step
operation7 = list1[6:1:-2]

#append() method to add elements at last position
list1.append(55)
print(list1)

#insert() method to insert element at specific position
list1.insert(5,25)
print(list1)




















