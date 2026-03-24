# Program to handle division by zero

try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
