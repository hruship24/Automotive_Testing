num =int (input('Enter number to check if Armstrong or not : '))

temp=num
summ = 0
while (num > 0):
    digit = num % 10
    summ += digit ** 3
    num //=10

if (temp == summ ):
    print('Armstrong Number')
else :
    print('Not Armstrong')
