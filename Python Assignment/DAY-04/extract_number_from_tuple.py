'''
Date : 22nd April 2024
Desc : Extract digits from tuples
'''

tuple1= (1,'b','c',3,'4','6',7,'d')
list1=[]

for val in tuple1:
    if str(val).isdigit():
        list1.append(int(val))

print('Extracted Values are : ',list1)
