'''
Date : 18th April 2024
Desc : Pyramid
'''

num1 = int(input('Enter the number of rows you want in pyramid: '))

for i in range(num1):
           for j in range(num1- i- 1):
                 print(' ',end='')

           for k in range(2 * i + 1):
                 print('*',end='')

           print()
