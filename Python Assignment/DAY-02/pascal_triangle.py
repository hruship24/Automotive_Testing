'''
Date : 18th April 2024
Desc : Pascal Triangle
formula : n!/k!(n-k)!
Pattern :
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
'''
num = int(input('Enter a number: '))

for i in range (num):

#adjust space
    print(' '* (num-i), end = "")

#compute each value in the row
    value = 1

    for j in range(0, i+1):

        print (value, end = " ")

        value = value *(i-j)//(j+1)

    print()
