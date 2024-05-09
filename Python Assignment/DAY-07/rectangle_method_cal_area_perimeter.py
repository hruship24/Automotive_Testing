'''
Date : 25th April 2024
Desc : Task-01 : Create a Python class named Rectangle with attributes
length and breadth and methods to calculate area and perimeter
'''

class Rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


length = int(input('Enter length of Rectangle : '))
breadth = int(input('Enter breadth of Rectangle : '))
rectangle = Rectangle(length, breadth)
print("Area of Rectanglre : ", rectangle.area())
print("Perimeter of Rectanglr : ", rectangle.perimeter())
