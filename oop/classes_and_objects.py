class Rectangle:

    # Constructor
    def __init__(self, x, y, length, breadth):
        self.x = x
        self.y = y
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def diagonal_point(self):
        return (self.x + self.length), (self.y + self.breadth)


rect = Rectangle(1, 1, 5, 5)
print("Area", rect.area())
print("Perimeter", rect.perimeter())
