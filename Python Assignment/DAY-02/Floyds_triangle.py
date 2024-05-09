'''
Date : 18th April 2024
Desc : Floyd's Triangle
'''
rows = int(input('Enter the number of rows for Floyd\'s triangle : '))

num=1

for i in range (1,rows+1):
    for j in range (1,i+1):
        print(num,end=' ')
        num +=1
    print()

    
