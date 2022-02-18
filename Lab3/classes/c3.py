from c2 import Shape

class Rectangle(Shape):
    def __init__(self, lenght: float, width: float):
        self.a = lenght
        self.b = width

    def area(self):
        print(self.a * self.b)

rect = Rectangle(5, 6)
rect.area()