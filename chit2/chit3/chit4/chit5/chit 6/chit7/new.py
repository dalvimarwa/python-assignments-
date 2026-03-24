# circle_module.py
import math

def area_circle():
    # Take radius from user
    r = float(input("Enter the radius of the circle: "))
    
    # Calculate area
    area = math.pi * (r ** 2)
    
    # Print result
    print("Area of the circle is:", area)
