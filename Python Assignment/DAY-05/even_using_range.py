'''
Date : 23rd April 2024
Desc : Write a python program using range function to print
       even numbers between intervel
'''

start = int(input('Enter start point : '))
end = int(input('Enter end point : '))

for i in range(start,end+1):
    if i % 2 == 0 :
        print(i)