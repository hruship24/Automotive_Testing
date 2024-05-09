from app.calculator import add, div, mul, sub, intdiv

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


print('Addition ', add(num1, num2))

def call_intdiv():
    try:
        print(intdiv(num1, num2))
    except ZeroDivisionError:
        print('Error Zero Division')


print('Subtraction ', sub(num1, num2))
print('Multiplication ', mul(num1, num2))
print('Division ', div(num1, num2))