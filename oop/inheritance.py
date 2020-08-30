class Vehicle:
    
    def __init__(self, color, max_speed):
        self.color = color
        self.max_speed = max_speed
    

class Car(Vehicle):
    
    def __init__(self, color, max_speed, gear_count, brand):
        super().__init__(color, max_speed)
        self.max_speed = max_speed
        self.gear_count = gear_count
        self.brand = brand
        
    def print_details(self):
        print("Color:", self.color)
        print("Max Speed:", str(self.max_speed) + " Km/hr")
        print("Gear Count:", str(self.gear_count))
        print("Brand:", self.brand)


c1 = Car("Black", 220, 6, "Hyundai")
c1.print_details()
