class Shape:
    def area(self):
        print(0)

class Square(Shape):
    def __init__(self, lenght: float):
        self.l = lenght

    def area(self):
        print(self.l**2)

if __name__ == '__main__':

    shape = Shape()
    square = Square(5)

    shape.area()
    square.area()