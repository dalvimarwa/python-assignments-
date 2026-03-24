# Function without parameters and without return value
def find_greatest():
    # Step 1: Take input from user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Step 2: Compare the numbers
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num2 > num1:
        print(f"{num2} is greater than {num1}")
    else:
        print("Both numbers are equal")

# Step 3: Call the function
find_greatest()
