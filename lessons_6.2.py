
class Shape:
    """центр окружности"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point(Shape):

    def __init__(self, x, y, p_x, p_y):
        Shape.__init__(self, x, y)
        self.p_x = p_x
        self.p_y = p_y

class Cirle(Point):

    def __init__(self, x, y, p_x, p_y, radius):
        Point.__init__(self, x, y, p_x, p_y)
        self.radius = radius

    def contains(self):
        print(self.p_x >= self.x and self.p_y >= self.y and self.p_x <= self.x+self.radius and self.p_y <= self.y+self.radius)


centre_point = Shape(10, 10)
point_point = Point(10, 10, 11, 11)
cirle_point = Cirle(10, 10, 9, 18, 18)
cirle_point.contains()

print(issubclass(Point, Shape))
print(issubclass(Cirle, Point))
print(issubclass(Cirle, Shape))