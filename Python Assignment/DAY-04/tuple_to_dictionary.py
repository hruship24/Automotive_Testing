'''
Date : 22nd April 2024
Desc : Convert list of tuple into dictionary
'''

tuple_list = [(1,'a'),(2,'b'),(3,'c'),(4,'d')]

dict1={}

for key,val in tuple_list:
    dict1[key]=val

print(dict1)
