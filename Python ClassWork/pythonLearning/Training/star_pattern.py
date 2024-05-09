'''
Date : 18th April 2024
Desc : *
       * *
       * * *
'''

row_number = int(input('Enter the number of rows for pattern : '))
start = 1

while (start <= row_number) :
    column =1
    while column <= start:
        print('*',end=' ')

        column +=1
    print()
    start +=1
