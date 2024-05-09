import math


def perimeter_of_circle(radius):
    return  2 * math.pi * radius

def area_of_circle(radius):
    return  math.pi * math.pow(radius,2)

radius = int(input("Enter the radius of circle : "))
peri = perimeter_of_circle(radius)
area = area_of_circle(radius)

print('Perimeter of circle is ',peri)
print('Area of circle is ',area)