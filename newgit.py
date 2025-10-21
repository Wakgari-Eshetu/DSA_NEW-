# Doing some use full things that relate to inheritance 
# With simple project that calculates the shape of things
import math
class Shape:
    def __init__(self,name ):
        self.name = name 
    def pr(self):
        print("the shape is ",self.name)

class Rectangle(Shape):
    def __init__(self, length ,width):
        super().__init__("rectangle")
        self.length = length
        self.width  = width 
        super().pr()
    def area(self):
        print(f"the area is {self.length *self.width}")
    def perimeter(self):
        print(f"the perimeter is {2*(self.length + self.width)}")
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle ")
        self.radius = radius
        super().pr()
    def area(self):
        print(f"the area is {math.pi*(self.radius ** 2)}")
    def preimeter(self):
        print(f"the perimeter  is {2*self.radius*math.pi}")

print("wellcome to the shape calculator!")
print("which shape do want to calculate? \n 1.for rectangle \n 2.for circle  ")
v = int(input("Enter the shape you want to calculate:"))
match v:
    case 1:
        l = int(input("Enter the length:"))
        w = int(input("Enter the width:"))
        c = Rectangle(l,w)
        c.area()
        c.perimeter()
    case 2:
        r = int(input("Enter the radius:"))
        c = Circle(r)
        c.area()
        c.preimeter()
    case _:
        print("Invalid choice.")
