class Vehicle:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def move(self):
        print(f"\nThe Vehicle is moving!")


class Car(Vehicle):
    def __init__(self, brand, model, color, price):
        self.price = price
        super(). __init__(brand, model, color)

    def move(self):
        print(f"Driving")

class Plane(Vehicle):
    def __init__(self, brand, model, color, type):
        self.type = type
        super(). __init__(brand, model, color)

    def move(self):
        print(f"Flying")

car1 = Car("Mazda", "Mazda CX-5", "Red", "$42,020")
car1.move()
print(car1.price)

plane1 = Plane("Lockheed Martin", "F-22 Raptor", "Gray", "Stealth Tactical Fighter Jet")
plane1.move()
print(plane1.type)
           