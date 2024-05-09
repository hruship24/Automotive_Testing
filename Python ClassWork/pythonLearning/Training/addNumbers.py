def addN(numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


count = int(input('How many numbers : '))
numbers =[]
for i in range(count):
    numbers.append(int(input('Enter number : ')))
sum = addN(numbers)
print(sum)
