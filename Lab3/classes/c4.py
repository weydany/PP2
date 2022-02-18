class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def show(self):
        print(f'x: {self.x}')
        print(f'y: {self.y}')

    def move(self, a: int, b: int):
        self.x = a
        self.y = b

    def dist(self, a: int, b: int):
        print( ( (self.x - a)**2 + (self.y - b)**2 )**0.5 )

point_1 = Point(5, 5)
point_2 = Point(0, 0)

point_1.show()
point_1.move(3, 4)
point_1.show()
point_1.dist(point_2.x, point_2.y)

