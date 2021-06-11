class Vehicle:
    def __init__(self, color, max_speed):
        self.color = color
        # Private to the vehicle class
        self.__max_speed = max_speed

    def get_max_speed(self):
        return self.__max_speed

    def set_max_speed(self, max_speed):
        self.__max_speed = max_speed

    def print_details(self):
        print("Color:", self.color)
        print("Max Speed:", str(self.__max_speed) + " Km/hr")


class Car(Vehicle):
    def __init__(self, color, max_speed, gear_count, brand):
        super().__init__(color, max_speed)
        self.gear_count = gear_count
        self.brand = brand

    def print_details(self):
        super().print_details()
        print("Gear Count:", str(self.gear_count))
        print("Brand:", self.brand)


c1 = Car("Black", 220, 6, "Hyundai")
c1.print_details()
