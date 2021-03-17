from abc import ABC, abstractmethod


class Automobile(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass


class Car(Automobile):
    def __init__(self, make):
        super(Car, self).__init__()
        self.make = make
        print("A {} car has been initialised".format(self.make))

    # Need to implement all functions below this comment if inheriting from abstract class
    def start(self):
        pass

    def stop(self):
        pass

    def drive(self):
        pass


# c = Automobile()  # cant create objects of abstract class
honda = Car("Honda")
