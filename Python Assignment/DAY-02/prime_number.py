'''
Date : 18th April 2024
Desc : Print all prime numbers in an interval
'''

start_point = int(input('Enter the Start point for prime number : '))
end_point = int(input('Enter the End point for prime number : '))

for num in range (start_point , end_point+1):
    if num > 1:
        for i in range (2, (num//2)+1):
            if(num % i)==0:
                break
        else:
            print(num)
'''
10 -> factors  2 5 
25 -> factors  5 
36 -> factors  2, 3 , 4, 6, 9, 12, 18
'''
