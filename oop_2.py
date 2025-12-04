print("")
print("------Know the Area of the Rectangle------")

class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
        

    def area(self):
        return self.l*self.b
r = Rectangle(int(input("Enter the length:")),int(input("Enter the breadth:")))
print(r.area())
print("")
print("-------Know the PERIMETER of the Rectangle-------")
print("")

class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
        

    def perimeter(self):
        return 2*(self.l+self.b)
print("")
r = Rectangle(int(input("Enter the length:")),int(input("Enter the breadth:")))
print(r.perimeter())
print("")
print("------Know the Area of the Circle-------")
print("")

class Circle:
    def __init__(self,r):
        self.r = r

    def area(self):
        pi = 3.14
        return pi*self.r**2
print("")   
c = Circle(int(input("Enter the radius:")))
print(c.area())

