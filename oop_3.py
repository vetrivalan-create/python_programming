print()
print("------Know the AREA and PERIMETER of the Rectangle------")
print()

class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)


r = Rectangle(int(input("Enter the rectangle length: ")), int(input("Enter the rectangle breadth: ")))
print("Rectangle area:", r.area())
print("Rectangle perimeter:", r.perimeter())

print()
print("------Know the AREA and PERIMETER of the Circle------")
print()

import math
class Circle:
    def __init__(self, radius):
        self.r = radius

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r


c = Circle(int(input("Enter the circle radius: ")))
print("Circle area:", c.area())
print("Circle perimeter:", c.perimeter())


sum_of_the_Area = r.area() + c.area()
print("Sum of areas (rectangle + circle):", sum_of_the_Area)

sum_of_the_Perimeter = r.perimeter() + c.perimeter()  
print("Sum of perimeters (rectangle + circle):", sum_of_the_Perimeter)

print()
print("--------THANK YOU-------")
print()
