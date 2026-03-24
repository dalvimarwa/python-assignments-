# Define Guitar class
class Guitar:
    def play(self):
        print("Playing Guitar")

# Define Piano class
class Piano:
    def play(self):
        print("Playing Piano")

# Function that accepts any object and calls its play method
def play_instrument(obj):
    obj.play()

# Create objects
guitar = Guitar()
piano = Piano()

# Demonstrate polymorphism
play_instrument(guitar)  # Output: Playing Guitar
play_instrument(piano)   # Output: Playing Piano
