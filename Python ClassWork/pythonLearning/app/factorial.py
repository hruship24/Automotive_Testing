# Stub
def facto(num):
    fact = 1
    for i in range(2, num+1):
        fact = i * facto(num-1)
    return fact

# Driver
# num = int(input('Enter the number : '))
# print('Factorial of ', num, ' is ', facto(num))
