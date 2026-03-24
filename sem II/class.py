# Base Class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")


# Subclass Car
class Car(Vehicle):
    def move(self):
        # Overriding move() method
        print("Driving on the road")


# Subclass Bicycle
class Bicycle(Vehicle):
    def move(self):
        # Overriding move() method
        print("Pedaling on the road")


# Demonstrating Polymorphism
def demonstrate_movement(vehicle):
    vehicle.move()   # Same method name, different behavior


# Creating objects
car = Car()
bicycle = Bicycle()

# Calling the same method on different objects
demonstrate_movement(car)
demonstrate_movement(bicycle)