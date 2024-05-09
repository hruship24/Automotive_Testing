'''
Date : 23rd April 2024
Desc : Check whether a number has consecutive 0’s in its binary equivalent
'''

def has_consecutive_zeros(num):
    binary_str = bin(num)[2:]
    consecutive_zeros = 0

    for bit in binary_str:
        if bit == '0':
            consecutive_zeros += 1
            if consecutive_zeros >= 2:
                return True
        else:
            consecutive_zeros = 0

    return False


number = int(input("Enter a number: "))
if has_consecutive_zeros(number):
    print("The number has consecutive zeros in its binary representation.")
else:
    print("The number doesn't have consecutive zeros in its binary representation.")