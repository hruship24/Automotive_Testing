'''
Date : 23rd April 2024
Desc : difference between sum of odd and even digits n given number
'''

def sum_odd(num) :
    odd_sum =1
    for i in num:
        if i % 2 == 0 :
            odd_sum += i
    return odd_sum

def sum_even(num) :
    even_sum = 1
    for i in num:
        if i % 2 != 0:
            even_sum += i
    return even_sum

num=[]
count = int(input('How many numbers you want to enter : '))
for i in range(1,count+1):
    val=int(input("Enter number : "))
    num.append(val)

odd_sum = sum_odd(num)
print('Sum of odd numbers from given : ',odd_sum)
even_sum = sum_even(num)
print('Sum of even numbers from given : ',even_sum)
difference = odd_sum - even_sum
print('Difference of sum of even and odd numbers is ',difference)
