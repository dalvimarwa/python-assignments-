# Define class Circle
class Circle:
    def draw(self):
        print("Drawing a Circle")

# Define class Square
class Square:
    def draw(self):
        print("Drawing a Square")

# Function that accepts any object and calls its draw method
def draw_shape(obj):
    obj.draw()

# Create objects
circle = Circle()
square = Square()

# Demonstrate polymorphism
draw_shape(circle)   # Output: Drawing a Circle
draw_shape(square)   # Output: Drawing a Square
