class Mother:
    def __init__(self):
        self.name = "Vaishali"

    def print(self):
        print("print function of Mother class")


class Father:
    def __init__(self):
        self.name = "Mohan"

    def print(self):
        print("print function of Father class")


class Child(Father, Mother):
    def __init__(self, name):
        self.name = name

    def print(self):
        super().print()


child = Child("Aditya")
child.print()  # calls print function of father since it comes first in the argument order of inheritance
Child.mro()  # prints the method resolution order
