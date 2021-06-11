from math import sqrt


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __str__(self):
        return "This point is at ({x}, {y})".format(x=self.__x, y=self.__y)

    # addition
    def __add__(self, other):
        return Point(self.__x + other.__x, self.__y + other.__y)

    # less than
    def __lt__(self, other):
        return sqrt(self.__x ** 2 + self.__y ** 2) < sqrt(
            other.__x ** 2 + other.__y ** 2
        )


p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)
print(p1 < p2)
