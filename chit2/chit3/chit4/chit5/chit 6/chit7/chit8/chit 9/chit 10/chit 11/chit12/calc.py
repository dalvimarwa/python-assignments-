# Class to demonstrate polymorphism
class Calculator:
    def add(self, *args):  # *args allows variable number of arguments
        if len(args) == 1:
            print("Sum of 1 value:", args[0])
        elif len(args) == 2:
            print("Sum of 2 values:", args[0] + args[1])
        elif len(args) == 3:
            print("Sum of 3 values:", args[0] + args[1] + args[2])
        else:
            print("This method supports 1, 2, or 3 values only.")

# Create object
calc = Calculator()

# Demonstrate polymorphism
calc.add(10)            # 1 value
calc.add(10, 20)        # 2 values
calc.add(5, 15, 25)     # 3 values
