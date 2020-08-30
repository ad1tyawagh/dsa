class Circle(object):

    # Object class provides 3 methods by default.
    # __new__  -  Used to create a new object
    # __init__ -  Used to initialise the object
    # __str__  -  Used to set a doc string for the class.

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "This class takes in a parameter 'radius', and creates a circle of radius equal to radius"


c = Circle(3)
print(c)
