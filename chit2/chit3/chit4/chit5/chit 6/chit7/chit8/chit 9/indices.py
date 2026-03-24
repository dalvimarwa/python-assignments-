# Program to print elements in a specific index range

# Step 1: Create a list
numbers = [10, 20, 30, 40, 50, 60, 70]

# Step 2: Take start and end indices from user
start = int(input("Enter starting index: "))
end = int(input("Enter ending index: "))

# Step 3: Slice the list
print("Elements in the given range:", numbers[start:end])
